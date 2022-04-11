import copy
import re
import csv
import subprocess
import os
import json
from pylint.lint import Run
import urllib
import sys
from models.module_metrics import CommitLog

# -- Load values from .env rather than hard-code them.
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()  # take environment variables from .env.
config = dotenv_values('.env')
ROOT_DIRECTORY = os.getenv('ROOT_DIRECTORY')
CURATED_HOME_DIRECTORY = os.getenv('CURATED_PROJECTS_FOLDER')
REPOSITORY_DATA_PATH = ROOT_DIRECTORY + '/code-metrics-alison/data/'

MASTER_REPO_DATA_FILE_PATH = REPOSITORY_DATA_PATH + os.getenv('MASTER_REPO_DATA_FILE')
MASTER_REPO_DATA_FILE_WITH_METRICS_PATH = REPOSITORY_DATA_PATH + os.getenv('MASTER_REPO_DATA_FILE_METRICS')
ERRORS_LOG_PATH = REPOSITORY_DATA_PATH + os.getenv('ERROR_LOGS')
DETAIL_COMPLEXITY_METRICS = REPOSITORY_DATA_PATH + os.getenv('DETAIL_COMPLEXITY_METRICS')


class CloneError(Exception):
    pass


class Repo:
    REPO_METRIC_KEYS = [  # pylint metrics
        'convention', 'refactor', 'method', 'function', 'class', 'code_lines', 'total_lines',
        'global_note', 'docstring_lines', 'statement', 'empty_lines',
        # git metrics
        'n_commits', 'n_bugs',
        # radon raw metrics
        'comments', 'loc', 'single_comments', 'lloc', 'multi', 'blank', 'sloc',
        # radon complexity metrics
        'number_of_methods', 'number_of_classes', 'number_of_functions', 'complexity', 'error']

    def metric_keys():
        return ['repo_name', 'module_name'] + Repo.REPO_METRIC_KEYS

    def to_short_name(self, module_path: str):
        return module_path.replace(os.path.join(self._base_directory, self.repo_name), '').replace('/', '.').lstrip('.')

    def __init__(self, base_directory, repo_url, error_log):
        self._base_directory = base_directory
        self.repo_url = repo_url
        self.error_log = error_log

        '''extract repo name, last section of url path'''
        self.repo_name = urllib.parse.urlparse(repo_url).path.split('/')[-1]

        # {module: {'git_metrics': List[CommitLogs], 'pylint_metrics': {}}
        self.metrics_by_module = {}

    def _is_package(self, dir_name):
        if 'test' not in dir_name and \
                'example' not in dir_name and \
                'script' not in dir_name and \
                'sample' not in dir_name and \
                '__init__.py' in os.listdir(dir_name):
            return True

        return False

    def modules(self):
        for dir_name, subdir_list, file_list in os.walk(os.path.join(self._base_directory, self.repo_name)):
            if self._is_package(os.path.join(dir_name)):
                for module in file_list:
                    if module.endswith('.py'):
                        yield os.path.join(dir_name, module)

    def clone(self, replace: bool = False, tag: str = None):
        print('-----> CLONING', self.repo_name)
        if not replace and self.repo_name in os.listdir(self._base_directory):
            '''nothing to do, repo already exists'''
            return

        self.free_space()
        os.chdir(self._base_directory)

        print('tag', tag)
        print('String to use for cloning:')
        if tag:
            print('     git', 'clone', '-b', tag, self.repo_url)
            result = subprocess.run(['git', 'clone', '-b', tag, self.repo_url], capture_output=True)
        else:
            print('     git', 'clone', self.repo_url)
            result = subprocess.run(['git', 'clone', self.repo_url], capture_output=True)

        m = re.search('Cloning into \'(.+)\'.*', str(result.stderr))

        if not m:
            raise CloneError()

    def free_space(self):
        os.system('rm -rf {}'.format(os.path.join(self._base_directory, self.repo_name)))

    def _parse_git_log(self, log):
        """format:
        [fb8e402ad] remitamine@gmail.com 2015-12-25 [hotstar] Add new extractor
        79      0       youtube_dl/extractor/hotstar.py"""

        line1_pattern = r'^\[([0-9abcdef]+)\](.*) ([0-9]{4}-[0-9]{2}-[0-9]{2}) (.*)$'
        line2_pattern = r'^([0-9]+)\s*([0-9]+)\s*.*$'

        lines = log.split('\n')

        if len(lines) < 2:
            self.error_log.write('could not split into two lines - {}'.format(log))

        m_line1 = re.search(line1_pattern, lines[0])
        m_line2 = re.search(line2_pattern, lines[1])

        if m_line1:
            author, date, message = m_line1.group(2), m_line1.group(3), m_line1.group(4)
        else:
            author, date, message = '-', '-', '-'

        if m_line2:
            lines_added, lines_deleted = m_line2.group(1), m_line2.group(2)
        else:
            lines_added, lines_deleted = 0, 0

        return CommitLog(author=author,
                         date=date,
                         message=message,
                         lines_added=lines_added,
                         lines_removed=lines_deleted)

    def generate_git_metrics(self):
        os.chdir(os.path.join(self._base_directory, self.repo_name))

        for module in self.modules():
            # git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat --
            try:
                result = subprocess.run(['git',
                                         'log',
                                         "--pretty=format:'[%h] %an %ad %s'",
                                         '--numstat',
                                         '--date=short',
                                         '--', module],
                                        encoding='utf-8',
                                        capture_output=True)

                log_parsed = result.stdout.split('\n\n')
            except Exception as e:
                self.error_log.write('module: {} - error git log: {}\n'.format(self.to_short_name(module), e))
                continue

            commit_logs = []
            for commit_text in log_parsed:
                try:
                    commit_logs.append(self._parse_git_log(commit_text.lstrip("\'\\\'")))
                except Exception as e:
                    self.error_log.write('module: {} - error git commit: {}\n'.format(self.to_short_name(module), e))
                    continue  # ignore commit and keep going with rest of commits

            module_metrics = self.metrics_by_module.get(module,
                                                        {'git_metrics': [], 'pylint_metrics': {}, 'radon_raw': {},
                                                         'radon_complexity': []})
            module_metrics['git_metrics'].extend(commit_logs)

            self.metrics_by_module[module] = module_metrics

    def generate_radon_raw_metrics(self):
        for module in self.modules():
            try:
                result = subprocess.run(['radon', 'raw', '-s', '--json', module], capture_output=True)

                # {"src/odf/xforms.py": {"loc": 33, "lloc": 8, "single_comments": 21, "sloc": 8, "multi": 0, "comments": 21, "blank": 4}}
                result_json = json.loads(result.stdout)
            except Exception as e:
                self.error_log.write('module: {} - error radon raw {}\n'.format(self.to_short_name(module), e))
                continue

            module_metrics = self.metrics_by_module.get(module,
                                                        {'git_metrics': [], 'pylint_metrics': {}, 'radon_raw': {},
                                                         'radon_complexity': []})

            module_metrics['radon_raw'] = list(result_json.values())[0]

            self.metrics_by_module[module] = module_metrics

    def generate_radon_complexity_metrics(self):
        for module in self.modules():
            try:
                result = None
                result = subprocess.run(['radon', 'cc', '-s', '--json', module], capture_output=True)
                result_json = json.loads(result.stdout)

                if len(result_json) < 1:
                    # empty module
                    continue

                result_json = list(result_json.values())[0]

                if result_json[0].get('error'):
                    raise Exception

            except Exception as e:
                self.error_log.write('module: {} - error radon cc {}\n'.format(self.to_short_name(module), e))
                continue

            module_metrics = self.metrics_by_module.get(module,
                                                        {'git_metrics': [], 'pylint_metrics': {}, 'radon_raw': {},
                                                         'radon_complexity': []})

            functions = [x for x in result_json if x.get('type') == 'function']
            methods = [x for x in result_json if x.get('type') == 'method']
            classes = [x for x in result_json if x.get('type') == 'class']

            EMPTY_COMPLEXITY_DICT = {'name': None,
                                     'type': None,
                                     'complexity': None,
                                     'classname': None}

            complexity_records = []
            for fun in functions:
                r = copy.deepcopy(EMPTY_COMPLEXITY_DICT)
                r['name'] = fun.get('name')
                r['type'] = 'function'
                r['complexity'] = fun.get('complexity')
                r['classname'] = None
                complexity_records.append(r)

            for meth in methods:
                r = copy.deepcopy(EMPTY_COMPLEXITY_DICT)
                r['name'] = meth.get('name')
                r['type'] = 'method'
                r['complexity'] = meth.get('complexity')
                r['classname'] = meth.get('classname')
                complexity_records.append(r)

            for cls in classes:
                r = copy.deepcopy(EMPTY_COMPLEXITY_DICT)
                r['name'] = cls.get('name')
                r['type'] = 'class'
                r['complexity'] = cls.get('complexity')
                r['classname'] = None
                complexity_records.append(r)

            module_metrics['radon_complexity'] = complexity_records

            self.metrics_by_module[module] = module_metrics

    def generate_pylint_metrics(self):
        for module in self.modules():

            # result = subprocess.run(['pylint', '-j 4', '--disable=W,E', '--output-format=json', module], capture_output=True)
            #
            # messages_json=json.loads(result.stdout)
            #
            # C = R = 0
            # for msg in messages_json:
            #     if msg['type'] == 'convention':
            #         C += 1
            #     elif msg['type'] == 'refactor':
            #         R += 1
            #
            # self.metrics = {module: {'convention': C,
            #                          'refactor': R}
            #                 }

            try:
                pylint_report = Run(args=['--disable=E,W', '-ry', module], do_exit=False)
            except Exception as e:
                self.error_log.write(
                    'module: {} - error pylint --disable=E,W {}\n'.format(self.to_short_name(module), e))
                continue

            pylint_metrics = {}
            for k, v in pylint_report.linter.stats.items():  # This line does not work
                if k in ['convention', 'refactor', 'method', 'function', 'class', 'code_lines', 'total_lines',
                         'global_note', 'docstring_lines', 'statement', 'empty_lines']:
                    pylint_metrics.update({k: v})

            module_metrics = self.metrics_by_module.get(module,
                                                        {'git_metrics': [], 'pylint_metrics': {}, 'radon_raw': {},
                                                         'radon_complexity': {}})
            module_metrics.get('pylint_metrics').update(pylint_metrics)
            self.metrics_by_module[module] = module_metrics

    def n_modules(self):
        return len(self.metrics_by_module.keys())

    def print_metrics(self):
        if not self.metrics_by_module == {}:
            for k, v in self.metrics_by_module.items():
                print(
                    '{}: score - {}\tconvention - {}\trefactor - {}\tcode_lines - {}\tclass - {}\tn_commits - {}'.format(
                        k,
                        v['pylint_metrics'].get('global_note', '-'),
                        v['pylint_metrics'].get('convention', '-'),
                        v['pylint_metrics'].get('refactor', '-'),
                        v['pylint_metrics'].get('code_lines', '-'),
                        v['pylint_metrics'].get('class', '-'),
                        len(v['git_metrics'])))


if __name__ == '__main__':
    sys.setrecursionlimit(2000)

    with open(MASTER_REPO_DATA_FILE_PATH) as file, open(MASTER_REPO_DATA_FILE_WITH_METRICS_PATH, 'a') as output_file, open(
            DETAIL_COMPLEXITY_METRICS, 'a') as detail_complexity_metrics, open(ERRORS_LOG_PATH, 'a') as error_log:

        input_repos = csv.DictReader(file, delimiter=',')
        output_csv = csv.DictWriter(output_file, fieldnames=Repo.metric_keys())
        output_csv.writeheader()

        detail_metrics_csv = csv.DictWriter(detail_complexity_metrics,
                                            fieldnames=['repo_name', 'module_name', 'name', 'type', 'complexity',
                                                        'classname'])
        detail_metrics_csv.writeheader()

        n = 0
        for repo_record in input_repos:
            if n > 20:
                break
            n += 1

            repo = Repo(base_directory=CURATED_HOME_DIRECTORY,
                        repo_url=repo_record['repo_url'],
                        error_log=error_log)

            print('====== START:', repo.repo_name, '======')

            repo.clone(replace=True, tag=repo_record['latest_tag'])
            print('---> About to enter generate_git_metrics()')
            repo.generate_git_metrics()
            print('---> About to enter generate_pylint_metrics()')
            repo.generate_pylint_metrics()
            print('---> About to enter generate_radon_raw_metrics()')
            repo.generate_radon_raw_metrics()
            print('---> About to enter generate_radon_complexity_metrics()')
            repo.generate_radon_complexity_metrics()
            # repo.free_space()

            print('---> About to loop through repo.metrics_by_module.keys()')
            for module in repo.metrics_by_module.keys():
                row = {'repo_name': repo.repo_name, 'module_name': repo.to_short_name(module)}
                row.update(repo.metrics_by_module[module]['pylint_metrics'])
                row.update({'n_commits': len(repo.metrics_by_module[module]['git_metrics'])})
                row.update(repo.metrics_by_module[module]['radon_raw'])

                # summary module-level complexity metrics
                row.update({'complexity': max(
                    list(r['complexity'] for r in repo.metrics_by_module[module]['radon_complexity']), default=0)})
                row.update({'number_of_methods': len(
                    [r for r in repo.metrics_by_module[module]['radon_complexity'] if r['type'] == 'method'])})
                row.update({'number_of_classes': len(
                    [r for r in repo.metrics_by_module[module]['radon_complexity'] if r['type'] == 'class'])})
                row.update({'number_of_functions': len(
                    [r for r in repo.metrics_by_module[module]['radon_complexity'] if r['type'] == 'function'])})

                n_bugs = 0
                # for commit_log in repo.metrics_by_module[module]['git_metrics']:
                #     if commit_log.is_bug:
                #         n_bugs += 1

                row.update({'n_bugs': n_bugs})

                output_csv.writerow(row)

            print('---> About to loop through repo.metrics_by_module.keys()')
            for module in repo.metrics_by_module.keys():
                row = {'repo_name': repo.repo_name, 'module_name': repo.to_short_name(module)}
                for complexity_record in repo.metrics_by_module[module]['radon_complexity']:
                    row.update(complexity_record)
                    detail_metrics_csv.writerow(row)

            error_log.write('{} processed successfully\n'.format(repo_record['full_name']))
            print('====== FINISH:', repo.repo_name, '======')
            repo = None

            print('---> End of file for generate_metrics.py')
