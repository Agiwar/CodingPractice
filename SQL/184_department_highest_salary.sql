-- solution 1: use DENSE_RANK to find out rank = 1
WITH cte AS (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS r
    FROM
        Employee
)
SELECT
    d.name     AS Department,
    cte.name   AS Employee,
    cte.salary AS Salary
FROM
    cte
INNER JOIN
    Department AS d
    ON cte.departmentId = d.id
WHERE
    cte.r = 1


-- solution 2: use MAX window function to find out the highest salary
WITH cte AS (
    SELECT
        name,
        salary,
        departmentId,
        MAX(salary) OVER(PARTITION BY departmentId) AS salary_highest
    FROM
        Employee
)
SELECT
    d.name AS Department,
    cte.name AS Employee,
    cte.salary AS Salary
FROM
    cte
INNER JOIN
    Department AS d
    ON cte.departmentId = d.id
WHERE
    cte.salary = cte.salary_highest