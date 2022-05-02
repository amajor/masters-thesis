-- https://radon.readthedocs.io/en/latest/commandline.html#the-raw-command
-- The equation sloc+multi+singlecomments+blank=loc should always hold.

SELECT
	t1_radon_raw.name AS "Repository",
    t1_radon_raw.module_name AS "Code Module",
    t2_radon_mi.mi AS "Maintainability Index",
	t1_radon_raw.loc AS "Total Lines of Code",
    
    CASE
      WHEN t1_radon_raw.sloc::numeric <> 0
      THEN CONCAT(TRUNC(t1_radon_raw.comments::numeric / t1_radon_raw.sloc::numeric * 100, 2), '%')
      ELSE 'NA'
    END AS "Comment-to-SLOC Ratio",
    
    t1_radon_raw.lloc AS "Logical Lines of Code",
    t1_radon_raw.single_comments AS "Single Line Comments (Only #)",
    t1_radon_raw.sloc AS "Source Lines of Code",
    t1_radon_raw.multi AS "Multi-Line Strings",
    t1_radon_raw.comments AS "Comments",
    t1_radon_raw.blank AS "Blank Lines"
FROM new_radon_raw_metrics AS t1_radon_raw
INNER JOIN new_radon_mi_metric AS t2_radon_mi
	ON t1_radon_raw.module_name = t2_radon_mi.module_name;
