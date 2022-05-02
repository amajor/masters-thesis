import copy
from typing import List
import re
import csv
import subprocess
import os
import json
from pylint.lint import Run
import urllib
import sys
from models.module_metrics import CommitLog
from generate_metrics import Repo
from datastore.pg_store import PgDataStore


# -- Load values from .env rather than hard-code them.
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()  # take environment variables from .env.
config = dotenv_values('.env')
ROOT_DIRECTORY = os.getenv('ROOT_DIRECTORY')
REPOSITORY_DATA_PATH = ROOT_DIRECTORY + '/code-metrics/data/'
MASTER_REPO_DATA_FILE_PATH = REPOSITORY_DATA_PATH + os.getenv('MASTER_REPO_DATA_FILE')


# TODO: exclude certain modules such as samples, test, etc.

class GitClient:
    COMMIT_RECORD = {
        "name": None,
        "module_name": None,
        "commit_digest": None,
        "author": None,
        "commited_at": None,
        "commit_msg": None,
        "lines_added": 0,
        "lines_removed": 0,
        "bug": 0
    }

    def __init__(self, repo: Repo):
        self._repo = repo

    def _parse_git_log(self, log) -> List[CommitLog]:
        '''format:
        [fb8e402ad] remitamine@gmail.com 2015-12-25 [hotstar] Add new extractor
        79      0       youtube_dl/extractor/hotstar.py
        80      1       youtube_dl/extractor/sample.py'''

        line1_pattern = r'^\[([0-9abcdef]+)\](.*) ([0-9]{4}-[0-9]{2}-[0-9]{2}) (.*)$'
        line2_pattern = r'^([0-9]+)\s*([0-9]+)\s*(.*)$'

        lines = log.split('\n')

        if len(lines) < 2:
            print('could not split into two lines - {}'.format(log))
            return []

        m_line1 = re.search(line1_pattern, lines[0])
        if m_line1:
            digest, author, date, message = m_line1.group(1).strip(), m_line1.group(2).strip(), m_line1.group(3), m_line1.group(4)
        else:
            digest, author, date, message = '-', '-', '-', '-'

        commit_logs = []
        for line in lines[1:]:
            module_line = re.search(line2_pattern, line)
            if module_line:
                lines_added, lines_deleted, module = module_line.group(1), module_line.group(2), module_line.group(3)
            else:
                continue

            commit_log = CommitLog(author=author,
                                   date=date,
                                   message=message.rstrip("'\\'"),
                                   lines_added=lines_added,
                                   lines_removed=lines_deleted,
                                   module=self._repo.to_short_name(module))

            commit = copy.deepcopy(GitClient.COMMIT_RECORD)
            commit['name'] = self._repo.repo_name
            commit['module_name'] = self._repo.to_short_name(module)
            commit['commit_digest'] = digest
            commit['author'] = author
            commit['commited_at'] = date
            commit['commit_msg'] = message.rstrip("'\\'")
            commit['lines_added'] = lines_added
            commit['lines_removed'] = lines_deleted
            commit['bug'] = 1 if commit_log.is_bug else 0

            commit_logs.append(commit)

        return commit_logs

    def get_commits_by_modules(self) -> dict:
        os.chdir(os.path.join(self._repo._base_directory, self._repo.repo_name))

        try:
            result = subprocess.run(['git',
                                     'log',
                                     "--pretty=format:'[%h] %an %ad %s'",
                                     '--numstat',
                                     '--date=short',
                                     '--'],
                                    encoding='utf-8',
                                    capture_output=True)

            log_parsed = result.stdout.split('\n\n')

            commit_logs = []
            for commit_text in log_parsed:
                commit_logs.extend(self._parse_git_log(commit_text.lstrip("\'\\\'")))

            # filter out commits with 0 added, deleted lines --> e.g., file rename, ignore for now
            commit_logs = list(filter(lambda x: not (x['lines_added'] == 0 and x['lines_removed'] == 0), commit_logs))

            # group commits by modules

            #            commits_by_module = {}
            #            for commit in commit_logs:
            #                module = commit.module
            #                commits_for_module = commits_by_module.get(module, [])

            #                commits_for_module.append(commit)
            #                commits_by_module[module] = commits_for_module

            return commit_logs

        except Exception as e:
            raise e


if __name__ == '__main__':
    with open(MASTER_REPO_DATA_FILE_PATH) as repo_input_file:
        input_repos_csv = csv.DictReader(repo_input_file, delimiter=',')

        n = 0
        for repo_record in input_repos_csv:

            if n > 7:
                break
            n += 1
            print('processing project: {}'.format(repo_record['full_name']))
            repo = Repo(base_directory='/home/omari/curated-python-projects',
                        repo_url=repo_record['repo_url'],
                        error_log=None)

            repo.clone(replace=True, tag=repo_record['latest_tag'])


            pg_store = PgDataStore()

            git_client = GitClient(repo=repo)
            commits = git_client.get_commits_by_modules()
            pg_store.store_git_metrics(commits)

            pg_store.close()
