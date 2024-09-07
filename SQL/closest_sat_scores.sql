WITH cte AS (
    SELECT
        student,
        score,
        LEAD(student, 1) OVER(ORDER BY score) AS next_student,
        LEAD(score, 1) OVER(ORDER BY score) AS next_score,
        ABS(score - LEAD(score, 1) OVER(ORDER BY score)) AS score_diff
    FROM
        scores
)

SELECT
    student AS one_student,
    next_student AS other_student,
    score_diff
FROM
    cte
WHERE
    score_diff = (SELECT MIN(score_diff) FROM cte)
-- If there are multiple students with the same minimum score difference, 
-- select the student name combination that is higher in the alphabet.
ORDER BY        
    one_student
LIMIT 1