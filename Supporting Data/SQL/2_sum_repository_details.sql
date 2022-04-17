-- https://radon.readthedocs.io/en/latest/commandline.html#the-raw-command
-- The equation sloc+multi+singlecomments+blank=loc should always hold.

SELECT
	t1_radon_raw.name AS "Repository",
    TRUNC(AVG(t2_radon_mi.mi::numeric), 2) AS "Average Project MI",
	SUM(t1_radon_raw.sloc::numeric) AS "Total Project SLOC",
	SUM(t1_radon_raw.comments::numeric) AS "Total Project Comments",
    CONCAT(TRUNC(
      SUM(t1_radon_raw.comments::numeric) / SUM(t1_radon_raw.sloc::numeric) * 100, 
      2  -- Number of decimal places
    ), '%') AS "Total Project Comment-to-SLOC Ratio",
    COUNT(DISTINCT t1_radon_raw.module_name) AS "Total Modules in Project",
    SUM(
      CASE
        WHEN t3_python_metrics.code = 'R' THEN n::numeric
        ELSE 0
      END
    ) AS "Total Refactor Msgs",
    SUM(
      CASE
        WHEN t3_python_metrics.code = 'C' THEN n::numeric
        ELSE 0
      END
    ) AS "Total Convention Msgs",
    MAX(t4_repo_details.commit_count) AS "Repo Commit Count",
    MAX(t4_repo_details.contributer_count) AS "Repo Contributer Count",
    MAX(t4_repo_details.release_count) AS "Repo Release Count"
FROM new_radon_raw_metrics AS t1_radon_raw
INNER JOIN new_radon_mi_metric AS t2_radon_mi
	ON t1_radon_raw.module_name = t2_radon_mi.module_name
    INNER JOIN new_pylint_metrics_by_msg AS t3_python_metrics
    	ON t1_radon_raw.module_name = t3_python_metrics.module_name
        INNER JOIN new_repo_details AS t4_repo_details
        	ON t1_radon_raw.name = t4_repo_details.repo_name_2
GROUP BY t1_radon_raw.name
ORDER BY t1_radon_raw.name ASC;
