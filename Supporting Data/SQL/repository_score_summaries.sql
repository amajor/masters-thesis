SELECT
	name,
    SUM(n_refactor) AS total_refactor,
    SUM(n_convention) AS total_convention
FROM pylint_metrics
GROUP BY name
ORDER BY name ASC;

SELECT
	name,
    code,
    sum(n)
FROM pylint_metrics_by_msg
GROUP BY name, code
ORDER BY name ASC;





-- See total refactors per repository
SELECT
	name
    ,SUM(n_refactor) AS total_refactor
FROM pylint_metrics
GROUP BY name
ORDER BY total_refactor ASC;

-- See AVERAGE refactors per repository
SELECT
	name
    ,AVG(n_refactor) AS average_refactor
FROM pylint_metrics
GROUP BY name
ORDER BY average_refactor ASC;

-- See total conventions per repository
SELECT
	name
    ,SUM(n_convention) AS total_convention
FROM pylint_metrics
GROUP BY name
ORDER BY total_convention ASC;
