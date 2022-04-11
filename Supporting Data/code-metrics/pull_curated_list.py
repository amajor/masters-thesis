import time
import csv
import json
import copy
from github_client import SearchClient
from github_client import RepoUtil
from github_client import CURRATED_REPO_DICT

if __name__ == '__main__':
    search_client = SearchClient(size_range=(500, 1000000),
                                 stars=600,
                                 created_before='2015-01-01',
                                 pushed_to_after='2018-07-01')

    n_pages = search_client.n_pages()
    n_repos = search_client.n_repos()
    print('number of repos: {}\t number of pages {}'.format(n_repos, n_pages))

    currated_repos = []
    total_skipped_n_commits = total_skipped_n_contributers = total_skipped_ratio = 0
    for page in range(0, int(n_pages + 2)):
        print('page {}/{} completed'.format(page, n_pages))
        # time.sleep(5)
        repos_for_page = search_client.get_results_page(page)
        for repo in repos_for_page:
            print('\trepo {}/{} completed'.format(len(currated_repos), n_repos))
            # time.sleep(5)
            repo_stats = copy.deepcopy(CURRATED_REPO_DICT)
            repo_stats['full_name'] = RepoUtil.full_name(repo)
            repo_stats['description'] = RepoUtil.description(repo)
            repo_stats['repo_url'] = RepoUtil.repo_url(repo)
            repo_stats['stars'] = RepoUtil.n_stars(repo)
            repo_stats['watchers'] = RepoUtil.n_watchers(repo)
            repo_stats['size'] = RepoUtil.size(repo)
            repo_stats['topics'] = json.dumps(RepoUtil.topics(repo))
            repo_stats['number_of_commits'] = RepoUtil.n_commits(repo)
            repo_stats['number_of_contributers'] = RepoUtil.n_contributors(repo)
            repo_stats['languages'] = json.dumps(RepoUtil.language_ratios(repo))
            repo_stats['date_created'] = RepoUtil.date_created(repo)
            repo_stats['date_last_push'] = RepoUtil.date_pushed(repo)
            repo_stats['number_of_open_issues'] = RepoUtil.n_open_issues(repo)

            n_releases, latest_tag, latest_commit = RepoUtil.releases(repo)
            repo_stats['n_releases'] = n_releases
            repo_stats['latest_tag'] = latest_tag
            repo_stats['latest_commit_sha'] = latest_commit

            repo_stats['license'] = RepoUtil.license(repo)
            repo_stats['name'] = RepoUtil.name(repo)

            repo_stats['raw'] = json.dumps(repo)

            # if repo_stats['number_of_commits'] < 999:
            #     print('\t\tskipping repo {}. number of commits {}'.format(repo_stats['full_name'], repo_stats['number_of_commits']))
            #     total_skipped_n_commits += 1
            #     continue
            #
            # if repo_stats['number_of_contributers'] < 20:
            #     print('\t\tskipping repo {}. number of contributers {}'.format(repo_stats['full_name'], repo_stats['number_of_contributers']))
            #     total_skipped_n_contributers += 1
            #     continue

            python_ratio = 0.0
            languages_json = json.loads(repo_stats['languages'])
            for r in languages_json:
                if r['language'] == 'Python':
                    python_ratio = r['ratio']
                    break

            if python_ratio < 0.7:
                print('\t\tskipping repo {}. Python ratio {}'.format(repo_stats['full_name'], python_ratio))
                print(repo_stats['languages'])

                total_skipped_ratio += 1
                # continue

            currated_repos.append(repo_stats)

    output_file = open('currated_python_list_all_v7.csv', 'w')

    csv_output = csv.writer(output_file)

    csv_output.writerow(currated_repos[0].keys())

    for currated_repo in currated_repos:
        csv_output.writerow(currated_repo.values())

    print('total repos pulled: {}\t total skipped - n_commits: {}, n_contributers: {}, python ratio: {}'.format(
        len(currated_repos),
        total_skipped_n_commits,
        total_skipped_n_contributers,
        total_skipped_ratio))
    output_file.close()
