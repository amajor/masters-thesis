from generate_metrics import Repo
import copy
import re
import csv
import subprocess
import os
from pylint.lint import Run
from datastore.pg_store import PgDataStore

# -- Load values from .env rather than hard-code them.
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()  # take environment variables from .env.
config = dotenv_values('.env')
ROOT_DIRECTORY = os.getenv('ROOT_DIRECTORY')
REPOSITORY_DATA_PATH = ROOT_DIRECTORY + '/code-metrics-alison/data/'
CURATED_PROJECTS_FOLDER = os.getenv('CURATED_PROJECTS_FOLDER')
MASTER_REPO_DATA_FILE_PATH = REPOSITORY_DATA_PATH + os.getenv('MASTER_REPO_DATA_FILE')

# The number of repositories to gather metrics from (originally 5)
# Current file set in environment variables has 134 records.
REPO_INDEX_START = 40  # os.getenv('REPO_INDEX_START')
REPO_INDEX_END = 46  # os.getenv('REPO_INDEX_END')
PUSH_TO_DB = True  # os.getenv('PUSH_TO_DB')


class PylintClient:
    EMPTY_PYLINT_DICT = {'name': None,
                         'module_name': None,
                         'n_refactor': 0,
                         'n_convention': 0,
                         'statement': 0,
                         'global_note': 0
                         }

    def __init__(self, repo: Repo):
        self._repo = repo
        self._msg_code_map = {}

    def msg_type(self, msg):
        if not self._msg_code_map or self._msg_code_map == {}:
            raise Exception('not populated')

        code = self._msg_code_map[msg]
        return code[:1]

    def pylint_n_for_type(self, code):
        if not self._msg_code_map or self._msg_code_map == {}:
            raise Exception('not populated')

        total = 0
        for k, v in self._msg_code_map.items():
            if self.msg_type(k) == code:
                total = total + 1

        return total

    def pylint_n_refactors(self):
        return self.pylint_n_for_type('R')

    def pylint_n_conventions(self):
        return self.pylint_n_for_type('C')

    def populate_msg_types(self):
        result = subprocess.run(['pylint',
                                 "--list-msgs", ],
                                encoding='utf-8',
                                capture_output=True)
        msgs = result.stdout.split(':')

        p = re.compile(r'(.*) \(([C,R,E,W][0-9]+)\)')

        for msg in msgs:
            r = p.match(msg)
            if r:
                message_name = r.group(1)
                message_code = r.group(2)
                self._msg_code_map.update({message_name: message_code})

    def generate_pylint_metrics(self, module):

        try:
            pylint_report = Run(args=['--disable=E,W', '-ry', module], do_exit=False)

            pylint_metric_record = copy.deepcopy(PylintClient.EMPTY_PYLINT_DICT)

            pylint_metric_record['name'] = self._repo.repo_name
            pylint_metric_record['module_name'] = self._repo.to_short_name(module)
            pylint_metric_record['n_refactor'] = pylint_report.linter.stats.refactor  # .get('refactor', 0)
            pylint_metric_record['n_convention'] = pylint_report.linter.stats.convention  # .get('convention', 0)
            pylint_metric_record['statement'] = pylint_report.linter.stats.statement  # .get('statement', 0)
            pylint_metric_record['global_note'] = pylint_report.linter.stats.global_note  # .get('global_note', 0)

            metrics_by_msg = []
            for k, v in pylint_report.linter.stats.by_msg.items():  # ['by_msg'].items():
                d = {'name': self._repo.repo_name,
                     'module_name': self._repo.to_short_name(module),
                     'msg': k,
                     'n': v,
                     'code': self.msg_type(k)
                     }
                metrics_by_msg.append(d)

            return pylint_metric_record, metrics_by_msg

        except Exception as e:
            print('module: {} - error pylint --disable=E,W {}\n'.format(self._repo.to_short_name(module), e))
            return None, []


if __name__ == '__main__':
    # gc.enable()
    # gc.DEBUG_LEAK
    with open(MASTER_REPO_DATA_FILE_PATH) as repo_input_file:
        input_repos_csv = csv.DictReader(repo_input_file, delimiter=',')

        all_repos = [
            {
                'repo_url': r['repo_url'],
                'latest_tag': r['latest_tag'],
                'full_name': r['full_name']
            } for r in
            input_repos_csv
        ]

        n = 0
        current_index = REPO_INDEX_START
        # for repo_record in input_repos_csv[0: 5]:
        for repo_record in all_repos[REPO_INDEX_START: REPO_INDEX_END]:
            n += 1
            print('========================================================')
            print('  n: ', n)
            print('  current index:', current_index)
            current_index += 1
            print('  processing project: {}'.format(repo_record['full_name']))
            print('--------------------------------------------------------')
            repo = Repo(base_directory=CURATED_PROJECTS_FOLDER,
                        repo_url=repo_record['repo_url'],
                        error_log=None)

            repo.clone(replace=True, tag=repo_record['latest_tag'])

            pylint_client = PylintClient(repo=repo)
            pg_store = PgDataStore()

            print('-----> start pylint_client.populate_msg_types()')
            pylint_client.populate_msg_types()
            print('-----> end pylint_client.populate_msg_types()')

            if PUSH_TO_DB:
                print('------------ PUSHING TO DATABASE --------------------------')
                for module in repo.modules():
                    metrics_summary, metrics_by_msg = pylint_client.generate_pylint_metrics(module=module)

                    pg_store.store_pylint_by_msg(metrics_by_msg)
                    pg_store.store_pylint([metrics_summary] if metrics_summary else [])
                    metrics_summary = None
                    metrics_by_msg = None
                print('  PUSHED -----> '.format(repo_record['full_name']))
            else:
                print('------------ NOT PUSHING TO DATABASE --------------------------')
                print('  DID NOT PUSH -----> '.format(repo_record['full_name']))

            pg_store.close()

            print('============= END ==============')
            print('  last index:', current_index - 1)
            print('============= END ==============')
            # print('Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            # gc.collect()
            # print('Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            #
            # objgraph.show_most_common_types()
            # all_objects = muppy.get_objects()
            # sum1 = summary.summarize(all_objects)
            # summary.print_(sum1)
