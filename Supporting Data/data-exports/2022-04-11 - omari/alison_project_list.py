import csv

alison_org_list = '''ansible
astropy
crossbario
aws
beetbox
biopython
boto
buildbot
celery
cobbler
conda
cython
django
encode
spesmilo
fail2ban
RaRe-Technologies
spotify
matplotlib
MongoEngine
mitmproxy
mongodb
mopidy
networkx
paramiko
openstack
numba
pandas-dev
coleifer
getpelican
pypa
Pylons
ranger
getsentry
saltstack
scikit-image
scikit-learn
scrapy
getsentry
zzzeek
openstack
sympy
tornadoweb
web2py
pallets
rg3'''

alison_repo_list = '''ansible
astropy
autobahn-python
aws-cli
beets
biopython
boto
buildbot
celery
cobbler
conda
cython
django
django-rest-framework
electrum
fail2ban
gensim
luigi
matplotlib
mongoengine
mitmproxy
mongo-python-driver
mopidy
networkx
paramiko
nova
numba
pandas
peewee
pelican
pip
pyramid
ranger
raven-python
salt
scikit-image
scikit-learn
scrapy
sentry
sqlalchemy
swift
sympy
tornado
web2py
werkzeug
youtube-dl'''

alison_org_list = alison_org_list.split()
alison_repo_list = alison_repo_list.split()
alison_list = ['{}/{}'.format(org, alison_repo_list[i]) for i, org in enumerate(alison_org_list)]

with open('/home/omari/repo_metrics/data/master_repo_133.csv') as repo_input_file:
    input_repos_csv = csv.DictReader(repo_input_file, delimiter=',')
    output_repos = filter(lambda r: r['full_name'] in alison_list, input_repos_csv)

    with open('data/alison_list.csv', 'w') as out_file:
        writer = csv.DictWriter(out_file, input_repos_csv.fieldnames)
        writer.writeheader()
        writer.writerows(list(output_repos))
