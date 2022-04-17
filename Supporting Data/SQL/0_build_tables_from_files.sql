
CREATE TABLE new_pylint_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 500 ),
  n_refactor  INT,
  n_convention INT,
  statement INT,
  global_note FLOAT
);

COPY new_pylint_metrics 
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/data-exports/2022-04-11 - omari/db-dumps/pylint_metrics.csv'  
DELIMITER ',' 
CSV HEADER;

CREATE TABLE new_pylint_metrics_by_msg (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 500 ),
  msg  VARCHAR ( 50 ),
  code VARCHAR ( 50 ),
  n VARCHAR ( 50 )
);

COPY new_pylint_metrics_by_msg
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/data-exports/2022-04-11 - omari/db-dumps/pylint_metrics_by_msg.csv'  
DELIMITER ',' 
CSV HEADER;

CREATE TABLE new_radon_raw_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 500 ),
  loc VARCHAR ( 50 ),
  lloc VARCHAR ( 50 ),
  single_comments VARCHAR ( 50 ),
  sloc VARCHAR ( 50 ),
  multi VARCHAR ( 50 ),
  comments VARCHAR ( 50 ),
  blank VARCHAR ( 50 )
);

COPY new_radon_raw_metrics
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/data-exports/2022-04-11 - omari/db-dumps/radon_raw_metrics.csv'  
DELIMITER ',' 
CSV HEADER;

CREATE TABLE new_radon_complexity_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 500 ),
  entity_name VARCHAR ( 500 ),
  type VARCHAR ( 50 ),
  complexity VARCHAR ( 50 ),
  rank VARCHAR ( 50 ),
  indentation VARCHAR ( 50 ),
  classname VARCHAR ( 50 )
);

COPY new_radon_complexity_metrics
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/data-exports/2022-04-11 - omari/db-dumps/radon_complexity_metrics.csv'  
DELIMITER ',' 
CSV HEADER;

CREATE TABLE new_radon_mi_metric (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 500 ),
  MI  INT
);

COPY new_radon_mi_metric
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/data-exports/2022-04-11 - omari/db-dumps/radon_mi_metric.csv'  
DELIMITER ',' 
CSV HEADER;

CREATE TABLE new_repo_details (
  repo_full_name VARCHAR ( 250 ),
  description VARCHAR ( 500 ),
  url VARCHAR ( 500 ),
  stars_count INT,
  watchers_count INT,
  size_count INT,
  topics VARCHAR (350),
  commit_count INT,
  contributer_count INT,
  languages_list VARCHAR (9000),
  created_date TIMESTAMP,
  last_push_date TIMESTAMP,
  open_issues_count INT,
  release_count INT,
  latest_tag VARCHAR (50),
  latest_commit_sha VARCHAR (50),
  license VARCHAR (250),
  repo_name_2 VARCHAR (50),
  raw VARCHAR (9000),
  unknown_1 DECIMAL,
  unknown_2 INT
);

COPY new_repo_details
FROM '/Users/alisonmajor/Developer/masters-thesis/Supporting Data/code-metrics/data/master_repo_133.csv'  
DELIMITER ',' 
CSV HEADER;
