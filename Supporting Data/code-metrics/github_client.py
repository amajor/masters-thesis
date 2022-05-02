import requests
from requests.auth import HTTPBasicAuth
import json
import urllib.parse as urlparse
import copy
import csv
import time
import re

GITHUB_SEARCH_URL='https://api.github.com/search/repositories'
Q_PARAM = 'language:{language} stars:>{stars} created:<{created_YYYY_MM_DD} pushed:>{pushed_YYYY_MM_DD} size:{low}..{high}'
Q_PARAM_ALL = 'language:{language}'

HEADERS = {'Accept': 'application/vnd.github.mercy-preview+json'}

# Set the username and password
github_user = 'USER'
github_password = 'PASSWORD'

GITHUB_AUTH=HTTPBasicAuth(github_user, github_password)

CURRATED_REPO_DICT = {
    'full_name': None,
    'description': None,
    'repo_url': None,
    'stars': None,
    'watchers': None,
    'size': None,
    'topics': None,
    'number_of_commits': None,
    'number_of_contributers': None,
    'languages': None,
    'date_created': None,
    'date_last_push': None,
    'number_of_open_issues': None,
    'n_releases': None,
    'latest_tag': None,
    'latest_commit_sha': None,
    'license': None,
    'name': None,
    'raw': None
}

class RepoUtil:
    def description(info: dict) -> str:
        """description of repo"""
        return info['description']

    def name(info: dict) -> str:
        """name"""
        return info['name']

    def full_name(info: dict) -> str:
        """full name"""
        return info['full_name']

    def url_html(info: dict) -> str:
        """github repo url"""
        return info['html_url']

    def n_watchers(info: dict) -> int:
        """number of watchers - DOES NOT SEEM ACCURATE"""
        # return info['watchers_count']
        WATCHERS_ROUTE = 'watchers'
        resp = requests.get(url=info['html_url'],
                            auth=GITHUB_AUTH)

        if resp.status_code != 200:
            raise Exception()

        try:
            resp_text = resp.text
            m = re.search(r'([0-9]+) users are watching this repository', resp_text)
            n_watchers = int(m.groups(0)[0])

            return n_watchers

        except:
            return 0


    def n_stars(info: dict) -> int:
        """stars"""
        return info['stargazers_count']

    def size(info: dict) -> int:
        """size of repo in bytes (I think)"""
        return info['size']

    def n_open_issues(info: dict) -> int:
        """number of open issues"""
        return info['open_issues_count']

    def repo_url(info: dict) -> str:
        """repo url"""
        return info['html_url']

    def date_created(info: dict) -> str:
        """date repo was created"""

        return info['created_at']

    def date_pushed(info: dict) -> str:
        """date repo was last pushed"""

        return info['pushed_at']

    def n_contributors(info: dict) -> int:
        """approximate number of contributers"""
        resp = requests.get(url=info['contributors_url'],
                            auth=GITHUB_AUTH)

        if resp.status_code != 200:
            raise Exception()

        try:
            if not resp.links:
                return len(resp.json())


            last = resp.links['last']['url']

            parsed = urlparse.urlparse(last)
            last_page = int(urlparse.parse_qs(parsed.query)['page'][0])

            contributers_per_page = len(resp.json())

            # get contributers on last page
            n_contributers_last_page = len(requests.get(url=last, auth=GITHUB_AUTH).json())

            return (last_page - 1)  * contributers_per_page + n_contributers_last_page

        except:
            return 0

    def releases(info: dict):
        """returns number of releases and last release tag"""
        resp = requests.get(url=info['tags_url'], auth=GITHUB_AUTH)

        if resp.status_code != 200:
            raise Exception()

        resp_j = resp.json()

        n_releases = 0
        latest_tag = None
        commit_sha = None


        if len(resp_j) > 0:
            latest_tag = resp_j[0]['name']
            commit_sha = resp_j[0]['commit']['sha']

        if not resp.links:
            n_releases = len(resp_j)
        else:
            last = resp.links['last']['url']
            parsed = urlparse.urlparse(last)
            last_page = int(urlparse.parse_qs(parsed.query)['page'][0])
            releases_per_page = len(resp_j)

            releases_on_last_page = len(requests.get(url=last, auth=GITHUB_AUTH).json())

            n_releases = (last_page - 1) * releases_per_page + releases_on_last_page

        return (n_releases, latest_tag, commit_sha)

    def n_commits(info: dict) -> int:

        """approximation of number of commits"""
        time.sleep(2)
        resp = requests.get(url=info['commits_url'].rstrip('{/sha}')+'s',
                            auth=GITHUB_AUTH)

        if resp.status_code != 200:
            print('{}: {}'.format(resp.status_code, resp.text))
            raise Exception()

        try:
            if not resp.links:
                #no pagination
                return len(resp.json())

            last = resp.links['last']['url']
            parsed = urlparse.urlparse(last)
            last_page = int(urlparse.parse_qs(parsed.query)['page'][0])

            n_commits_last_page = len(requests.get(url=last, auth=GITHUB_AUTH).json())


            commits_per_page = len(resp.json())
            # get commits on last page

            return (last_page - 1) * commits_per_page + n_commits_last_page
        except:
            return 0

    def language_ratios(info: dict):
        """dict with languages and their LOC ratio"""
        resp = requests.get(url=info['languages_url'], auth=GITHUB_AUTH)
        languages_json = resp.json()
        total = 0
        for pairs in languages_json.items():
            total += pairs[1]

        languages = []
        for k, v in languages_json.items():
            languages.append({'language': k, 'loc': v, 'ratio': v/total })

        return languages

    def topics(info: dict):
        """project topics"""
        return json.dumps(info['topics'])

    def default_branch(info: dict) -> str:
        return info['default_branch']

    def n_open_issues(info: dict) -> int:
        """number of open issues"""
        return info['open_issues_count']

    def license(info: dict):
        """retruns license as a dict"""
        return json.dumps(info['license'])

class SearchClient:
    def __init__(self,
                 size_range = (0, 10000000),
                 language: str = 'Python',
                 stars: int = 10000,
                 created_before: str = '2015-01-01',
                 pushed_to_after: str = '2018-06-01'):

        self.language = language
        self.stars = stars
        self.created_before = created_before
        self.pushed_to_after = pushed_to_after
        self.per_page = 50
        self.size_range = size_range

    def _do_get_request(self,
                        low,
                        high,
                        page = 1):

        resp = requests.get(url=GITHUB_SEARCH_URL,
                            params={'q': Q_PARAM.format(low=low if low else self.size_range[0],
                                                        high=high if high else self.size_range[1],
                                                        language=self.language,
                                                        stars=self.stars,
                                                        created_YYYY_MM_DD=self.created_before,
                                                        pushed_YYYY_MM_DD=self.pushed_to_after),
                                    'page': page,
                                    'per_page': 30},

                            headers=HEADERS,
                            auth=HTTPBasicAuth('safwan-lewis', 'ManiHani1024'))

        if resp.status_code != 200:
            raise Exception

        return resp

    def n_pages(self):
        try:
            resp = self._do_get_request(low=self.size_range[0], high=self.size_range[1])
            last = resp.links['last']['url']

            parsed = urlparse.urlparse(last)
            last_page = int(urlparse.parse_qs(parsed.query)['page'][0])

            return last_page - 1

        except:
            return 0

    def get_results_page(self, page: int, min_size = None, max_size = None):
        resp = self._do_get_request(page=page,
                                    low=min_size if min_size else self.size_range[0],
                                    high=max_size if max_size else self.size_range[1])

        return resp.json()['items']


    def n_repos(self):
        resp = self._do_get_request(low=self.size_range[0], high=self.size_range[1])
        return resp.json()['total_count']


