SELECT
    id,
    CASE 
        WHEN id % 2 = 1 THEN LEAD(student, 1, student) OVER()
        ELSE LAG(student, 1, student) OVER()
    END AS student
FROM
    Seat
ORDER BY
    id