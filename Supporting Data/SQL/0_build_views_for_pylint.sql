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

-- CONFIRM ALL MATCHING VALUES (should return 0 records)
SELECT *
FROM new_view_compare_pylint_metrics_for_validation
WHERE total_refactor_match = 'FALSE'
  OR total_convention_match = 'FALSE';
