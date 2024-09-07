SELECT
    student_name,
    MAX(CASE WHEN exam_id = 1 THEN score ELSE NULL END) AS exam_1,
    MAX(CASE WHEN exam_id = 2 THEN score ELSE NULL END) AS exam_2,
    MAX(CASE WHEN exam_id = 3 THEN score ELSE NULL END) AS exam_3,
    MAX(CASE WHEN exam_id = 4 THEN score ELSE NULL END) AS exam_4
FROM
    exam_scores
GROUP BY
    student_name