-- Check for Consistency!

-- This shows us the totals for Refactor and Convention from pylint_metrics
CREATE VIEW v_pylint_metrics_totals AS
SELECT
	name,
    SUM(n_refactor) AS total_refactor,
    SUM(n_convention) AS total_convention
FROM pylint_metrics
GROUP BY name
ORDER BY name ASC;


/*
SELECT
	name,
    sum(n) AS total_refactor
FROM pylint_metrics_by_msg
WHERE code = 'R'
GROUP BY name
ORDER BY name ASC;

SELECT
	name,
    sum(n) AS total_convention
FROM pylint_metrics_by_msg
WHERE code = 'C'
GROUP BY name
ORDER BY name ASC;
*/

-- This shows us the totals for Refactor and Convention from pylint_metrics_by_msg_totals
-- The values here should match the values found in the view above.
CREATE VIEW v_pylint_metrics_by_msg_totals AS
SELECT
	name,
    SUM(
      CASE
        WHEN code = 'R' THEN n
        ELSE 0
      END
    ) AS total_refactor,
    SUM(
      CASE
        WHEN code = 'C' THEN n
        ELSE 0
      END
    ) AS total_convention
FROM pylint_metrics_by_msg
GROUP BY name
ORDER BY name ASC;

-- This view will show us "FALSE" if any repository doesn't match when we compare
-- pylint_metrics and pylint_metrics_by_msg_totals
CREATE VIEW v_compare_pylint_metrics_for_validation AS
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
FROM v_pylint_metrics_totals AS v1
INNER JOIN v_pylint_metrics_by_msg_totals AS v2
  ON v1.name = v2.name;

SELECT *
FROM v_compare_pylint_metrics_for_validation
WHERE total_refactor_match = 'FALSE'
  OR total_convention_match = 'FALSE';