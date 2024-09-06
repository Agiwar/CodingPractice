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
    cte.r IN (1, 2, 3)