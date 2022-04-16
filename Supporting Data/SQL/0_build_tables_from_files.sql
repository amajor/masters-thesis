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

-- Then we can create views from these data dumps.
-- This allows us to compare our data to see any misalignments.

-- Total refactor and convention messages from Pylint.
/*
SELECT
	name,
    SUM(n_refactor) AS total_refactor,
    SUM(n_convention) AS total_convention
FROM new_pylint_metrics
GROUP BY name
ORDER BY name ASC;
*/

CREATE VIEW new_view_pylint_metrics_totals AS
SELECT
	name,
    SUM(n_refactor) AS total_refactor,
    SUM(n_convention) AS total_convention
FROM new_pylint_metrics
GROUP BY name;

-- Total refactor and convention messages from Pylint Msg List.
/*
SELECT
	name,
    SUM(
      CASE
        WHEN code = 'R' THEN n::numeric
        ELSE 0
      END
    ) AS total_refactor,
    SUM(
      CASE
        WHEN code = 'C' THEN n::numeric
        ELSE 0
      END
    ) AS total_convention
FROM new_pylint_metrics_by_msg
GROUP BY name
ORDER BY name ASC;
*/

CREATE VIEW new_view_pylint_metrics_by_msg_totals AS
SELECT
	name,
    SUM(
      CASE
        WHEN code = 'R' THEN n::numeric
        ELSE 0
      END
    ) AS total_refactor,
    SUM(
      CASE
        WHEN code = 'C' THEN n::numeric
        ELSE 0
      END
    ) AS total_convention
FROM new_pylint_metrics_by_msg
GROUP BY name;

CREATE VIEW new_view_compare_pylint_metrics_for_validation AS
SELECT
  v1.name,
  CASE
    WHEN v1.total_refactor = v2.total_refactor
      THEN 'TRUE'
    ELSE 'FALSE'
  END AS total_refactor_match,
  CASE
    WHEN v1.total_convention = v2.total_convention
      THEN 'TRUE'
    ELSE 'FALSE'
  END AS total_convention_match,
  v1.total_refactor AS v1_total_refactor,
  v2.total_refactor AS v2_total_refactor,
  v1.total_convention AS v1_total_convention,
  v2.total_convention AS v2_total_convention
FROM new_view_pylint_metrics_totals AS v1
INNER JOIN new_view_pylint_metrics_by_msg_totals AS v2
  ON v1.name = v2.name;

-- CONFIRM ALL MATCHING VALUES
-- If both the pylint_metrics and pylint_metrics_by_msg tables have the same
-- number of messages for Refactor and Convention, then this query below
-- should return 0 records.
SELECT *
FROM new_view_compare_pylint_metrics_for_validation
WHERE total_refactor_match = 'FALSE'
  OR total_convention_match = 'FALSE';
