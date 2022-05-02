import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords


def decode_(paragraph: str):
    # sr = stopwords.words('english')

    lines = []
    f = open('./data/raw_description', 'rb')
    for line in f:
        try:
            line = line.decode(encoding='ascii')
            lines.append(line)
        except UnicodeDecodeError as e:
            print(e)

    tokens = ''.join(lines).split()

def remove_stop_words(paragraph: str):
    words_no_stop = []
    words = paragraph.split()
    for word in words:
        if word not in stopwords.words('english'):
            words_no_stop.append(word)

    freq = nltk.FreqDist(words)

    for key, val in freq.items():
        print(str(key) + ':' + str(val))

    return words_no_stop

MASTER_REPO_FILE_PATH='../data/currated_python_list_all_v6.csv'
FILTERED_REPO_FILE = '../data/currated_python_list_all_filtered_v6.csv'

def get_kmean_clusters(all_features):
    X = np.array(all_features)
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    return (centroids, labels)

if __name__ == '__main__':
    # with open(MASTER_REPO_FILE_PATH) as input_file, open(FILTERED_REPO_FILE, 'w') as output_file:
    #     input_repos = csv.DictReader(input_file, delimiter=',')
    #     output_csv = csv.DictWriter(output_file, fieldnames=input_repos.fieldnames)
    #     output_csv.writeheader()
    #
    #     all_features =[]
    #     all_repo_names = []
    #     all_description = []
    #     for repo_record in input_repos:
    #         repo_features = [repo_record['number_of_commits'], repo_record['watchers'], repo_record['number_of_contributers']]
    #         all_features.append(repo_features)
    #         all_repo_names.append(repo_record['name'])
    #         all_description.append(repo_record['description'])
    #
    #     topics = remove_stop_words(' '.join(all_description))
    with open('../data/description_for_missing_topics', 'r') as input_file:
        all_description = input_file.read()
        words = remove_stop_words(all_description)
        print(' '.join(words))











