WITH cte AS (
    SELECT
        e.salary AS salary,
        DENSE_RANK() OVER(PARTITION BY e.department_id ORDER BY e.salary DESC) AS rk
    FROM
        employees AS e
    INNER JOIN
        departments AS d
        ON e.department_id = d.id
    WHERE
        d.name = 'engineering'
)

SELECT DISTINCT
    salary
FROM
    cte
WHERE
    rk = 2