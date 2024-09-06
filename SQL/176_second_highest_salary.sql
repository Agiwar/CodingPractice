-- solution 1: dense_rank + cte
WITH cte AS (
    SELECT
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS r
    FROM
        Employee
)
SELECT 
    max(salary) AS SecondHighestSalary
FROM
    cte
WHERE
    r > 1


-- solution 2: limit + offset
WITH cte AS (
    SELECT DISTINCT
        salary
    FROM
        Employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1
)
SELECT
    max(salary) AS SecondHighestSalary
FROM
    cte