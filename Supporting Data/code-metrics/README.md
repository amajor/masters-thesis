# RUN

## pylint_client.py

This will generate metrics from Pylint and will push to the database.

Open using PyCharm. This has a lot of built-in help.

```python
# Execute the program using python.
python3 pylint_client.py
```

For thesis work, set the master file in `.env` to `thesis_filtered_repos.csv`:

This will shorten and limit the data you need to pull into the database. There are 46 total repositories in this list.

```dotenv
MASTER_REPO_DATA_FILE='thesis_filtered_repos.csv'
```

The list above was generating by filtering to repositories that meets the following criteria, calculated using the 20th percentile of values in the group:

- A long history of commits
  - 2968 commits or more [20th Percentile]
- Large development teams
  - 90 contributors or more [20th Percentile]
- 80% python or higher
- Many releases
  - 44 releases or more [20th Percentile]
- Substantial age
  - 66 months or older (5.5 years) [20th Percentile]

## radon_client.py

???

## generate_metrics.py

This will generate metrics in a file, but will not push to the database.

Open using PyCharm. This has a lot of built-in help.

```python
# Execute the program using python.
python3 generate_metrics.py
```

This will run for the first 20 repositories in the file listed under `MASTER_REPO_DATA_FILE` in the `.env` file.

Once it runs, make note of the last file completed, then remove the rows at and above that last repository in the `MASTER_REPO_DATA_FILE`. Then run again for the next batch.

### Troubleshooting

If you have trouble with executing the file, you may need to adjust permissions.

```shell
# This will let you see permissions for the file.
 ls -la

# This will allow you to execute the file you are adjusting.
chmod 755 ./generate_metrics.py
```

If you have trouble with **dotenv** being imported, try this:

```shell
pip install python-dotenv
```

#### Notes

The repository `gensim` is unable to be cloned in the expected sense.

When running `python3 generate_metrics.py` we fail:

```shell
Alisons-MacBook-Pro: ~/Developer/code-metrics-alison/curated-python-projects                                                                +[git:alison-course-project]
→  git clone -b 8.6 https://github.com/RaRe-Technologies/gensim
Cloning into 'gensim'...
fatal: Remote branch 8.6 not found in upstream origin
```

For now, we are skipping this repository.

# SETUP

You need a PostgreSQL database in order to run the program.

Suggested PostgreSQL client on Mac:
[Beekeeper Studio](https://www.beekeeperstudio.io/db/postgres-client/)

## Create .env File
You should have a file named `.env` in the root directory.

It should have values along these lines:

```dotenv
#-- GitHub credentials needed to access the public repositories
GITHUB_USER='the_user'
GITHUB_PASSWORD='the_password'

#-- The directory where the code-metrics folder resides.
#-- Example on Mac: '/Users/myuser/Developer/' or '/Users/myuser/Developer/curated-python-projects'
ROOT_DIRECTORY='/Users/myuser/Developer'
CURATED_PROJECTS_FOLDER='/Users/myuser/Developer/code-metrics/curated-python-projects'

#-- File Names
MASTER_REPO_DATA_FILE='master_repo_133.csv'
MASTER_REPO_DATA_FILE_METRICS='master_repo_133_with_metrics_radon_raw_mypy.csv'
DETAIL_COMPLEXITY_METRICS='detail_repo_133_radon_complexity_metrics_mypi.csv'
ERROR_LOGS='errors.log'
```

## Setup Database

### Mac

```shell
brew update

brew install postgresql
```

Then start the service!

```shell
brew services start postgresql
```

Create a database.

```shell
createdb python_list_dev
```

To stop it...

```shell
brew services stop postgresql
```

### Configure

```shell
psql postgres

# You will see the prompt
# postgres=#

# Create a new user called `postgres` and the password `admin123`
CREATE ROLE postgres WITH LOGIN PASSWORD 'admin123';

ALTER ROLE postgres CREATEDB;

# Quit the session
\q
```

See the users:

```shell
psql postgres -U postgres

# Lists the users
\du

# Quit the session
\q
```

## Create Tables in Database

```postgresql
CREATE TABLE pylint_metrics (
  name VARCHAR ( 255 ),
  module_name VARCHAR ( 255 ),
  n_refactor INT,
  n_convention INT,
  statement INT,
  global_note FLOAT
);

CREATE TABLE pylint_metrics_by_msg (
  name VARCHAR ( 255 ),
  module_name VARCHAR ( 255 ),
  msg  VARCHAR ( 255 ),
  code VARCHAR ( 255 ),
  n INT
);

CREATE TABLE git_metrics (
  name VARCHAR ( 255 ),
  module_name VARCHAR ( 255 ),
  commit_digest  VARCHAR ( 255 ),
  author VARCHAR ( 255 ),
  commited_at VARCHAR ( 255 ),
  commit_msg VARCHAR ( 255 ),
  lines_added VARCHAR ( 255 ),
  lines_removed VARCHAR ( 255 ),
  bug VARCHAR ( 255 )
);

CREATE TABLE radon_raw_metrics (
  name VARCHAR ( 255 ),
  module_name VARCHAR ( 255 ),
  loc VARCHAR ( 255 ),
  lloc VARCHAR ( 255 ),
  single_comments VARCHAR ( 255 ),
  sloc VARCHAR ( 255 ),
  multi VARCHAR ( 255 ),
  comments VARCHAR ( 255 ),
  blank VARCHAR ( 255 )
)

CREATE TABLE radon_complexity_details (
  name VARCHAR ( 255 ),
  module_name VARCHAR ( 255 ),
  entity_name VARCHAR ( 255 ),
  type VARCHAR ( 255 ),
  complexity VARCHAR ( 255 ),
  rank VARCHAR ( 255 ),
  indentation VARCHAR ( 255 ),
  classname VARCHAR ( 255 )
)
```
