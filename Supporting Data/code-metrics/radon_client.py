import csv
import time
from generate_metrics import Repo
import copy
import json
import subprocess
from datastore.pg_store import PgDataStore
import os

# -- Load values from .env rather than hard-code them.
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()  # take environment variables from .env.
config = dotenv_values('.env')
ROOT_DIRECTORY = os.getenv('ROOT_DIRECTORY')
REPOSITORY_DATA_PATH = ROOT_DIRECTORY + '/code-metrics/data/'
CURATED_PROJECTS_FOLDER = os.getenv('CURATED_PROJECTS_FOLDER')
MASTER_REPO_DATA_FILE_PATH = REPOSITORY_DATA_PATH + os.getenv('MASTER_REPO_DATA_FILE')


class RadonClient:
    EMPTY_COMPLEXITY_DICT = {'name': None,
                             'module_name': None,
                             'entity_name': None,
                             'type': None,
                             'complexity': 0,
                             'rank': None,
                             'indentation': None,
                             'classname': None
                             }

    EMPTY_RAW_METRICS_DICT = {'name': None,
                              'module_name': None,
                              'loc': 0,
                              'lloc': 0,
                              'single_comments': 0,
                              'sloc': 0,
                              'multi': 0,
                              'comments': 0,
                              'blank': 0
                              }

    EMPTY_MI_DICT = {'name': None,
                     'module_name': None,
                     'mi': -1
                     }


    def __init__(self, repo: Repo):
        self._repo = repo

    def generate_radon_raw_metrics(self, module, timeout=60 * 5):
        try:
            start = time.time()
            result = subprocess.run(['radon', 'raw', '-s', '--json', module], capture_output=True, timeout=timeout)
            duration = time.time() - start

            # {"src/odf/xforms.py": {"loc": 33, "lloc": 8, "single_comments": 21, "sloc": 8, "multi": 0, "comments": 21, "blank": 4}}
            result_json = json.loads(result.stdout)
            module_metrics = list(result_json.values())[0]

            raw_metrics = copy.deepcopy(RadonClient.EMPTY_RAW_METRICS_DICT)
            raw_metrics['name'] = repo.repo_name
            raw_metrics['module_name'] = repo.to_short_name(module)
            raw_metrics['loc'] = module_metrics.get('loc', 0)
            raw_metrics['lloc'] = module_metrics.get('lloc', 0)
            raw_metrics['single_comments'] = module_metrics.get('single_comments', 0)
            raw_metrics['sloc'] = module_metrics.get('sloc', 0)
            raw_metrics['multi'] = module_metrics.get('multi', 0)
            raw_metrics['comments'] = module_metrics.get('comments', 0)
            raw_metrics['blank'] = module_metrics.get('blank', 0)

            return (raw_metrics, duration)

        except Exception as e:
            print("radon raw subprocess failed - {}".format(e))
            raise e

    def generate_radon_complexity_metrics(self, module, timeout=60 * 5):
        try:
            start = time.time()
            result = subprocess.run(['radon', 'cc', '-s', '--json', module], capture_output=True, timeout=timeout)
            duration = time.time() - start

            result_json = json.loads(result.stdout)

            if len(result_json) < 1:
                # empty module
                return ([], duration)

            result_json = list(result_json.values())[0]

            if isinstance(result_json, dict) and result_json.get('error'):
                raise Exception

            complexity_records = []
            for entity in result_json:
                r = copy.deepcopy(RadonClient.EMPTY_COMPLEXITY_DICT)

                r['name'] = repo.repo_name
                r['module_name'] = repo.to_short_name(module)
                r['entity_name'] = entity.get('name')
                r['type'] = entity.get('function')
                r['complexity'] = entity.get('complexity')
                r['rank'] = entity.get('rank')
                r['indentation'] = entity.get('col_offset')
                r['classname'] = entity.get('classname')
                complexity_records.append(r)

            return (complexity_records, duration)


        except Exception as e:
            print('module: {} - error radon cc {}\n'.format(repo.to_short_name(module), e))
            return ([], duration)

    def generate_radon_mi(self, module, timeout=60 * 5):
        try:
            start = time.time()
            result = subprocess.run(['radon', 'mi', '-s', '--json', module], capture_output=True, timeout=timeout)
            duration = time.time() - start

            # {"ckan/logic/auth/publisher/create.py": {"mi": 60.72980893471243, "rank": "A"}}
            result_json = json.loads(result.stdout)
            module_metrics = list(result_json.values())[0]

            mi_metrics = copy.deepcopy(RadonClient.EMPTY_MI_DICT)
            mi_metrics['name'] = repo.repo_name
            mi_metrics['module_name'] = repo.to_short_name(module)
            mi_metrics['mi'] = round(module_metrics.get('mi', -1))

            return (mi_metrics, duration)

        except Exception as e:
            print("radon mi subprocess failed - {}".format(e))
            raise e

if __name__ == '__main__':
    with open(MASTER_REPO_DATA_FILE_PATH) as repo_input_file:
        input_repos_csv = csv.DictReader(repo_input_file, delimiter=',')

        n = 0
        for repo_record in input_repos_csv:
            if n > 100:
                break
            n += 1
            print('processing project: {}'.format(repo_record['full_name']))
            repo = Repo(base_directory=CURATED_PROJECTS_FOLDER,
                        repo_url=repo_record['repo_url'],
                        error_log=None)

            repo.clone(replace=False, tag=repo_record['latest_tag'])

            n_modules = len(list(repo.modules()))
            radon_client = RadonClient(repo=repo)
            pg_datastore = PgDataStore()

            for i, module in enumerate(repo.modules()):
                print('processing module/raw_metrics {} of {} - {}'.format(i, n_modules, repo.to_short_name(module)), end=' .... ')
                try:
                    raw_metrics, duration = radon_client.generate_radon_raw_metrics(module=module)
                    print('took: {} seconds'.format(duration))
                    pg_datastore.store_radon_raw_metrics(data=[raw_metrics])
                except:
                    print('FAIL')
                    continue

            for i, module in enumerate(repo.modules()):
                print('processing module/oo_metrics {} of {} - {}'.format(i, n_modules, repo.to_short_name(module)), end=' ..... ')
                oo_metrics, duration = radon_client.generate_radon_complexity_metrics(module=module)
                print('took: {} seconds'.format(duration))
                pg_datastore.store_radon_complexity_metrics(data=oo_metrics)

            for i, module in enumerate(repo.modules()):
                print('processing module/mi_metric {} of {} - {}'.format(i, n_modules, repo.to_short_name(module)), end=' ..... ')
                mi_metric, duration = radon_client.generate_radon_mi(module=module)
                print('took: {} seconds'.format(duration))
                pg_datastore.store_radon_mi_metric(data=mi_metric)

            pg_datastore.close()
