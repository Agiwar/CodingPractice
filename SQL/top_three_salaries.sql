WITH cte AS (
    SELECT
        CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
        e.salary AS salary,
        d.name AS department_name,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS rk
    FROM
        employees AS e
    INNER JOIN
        departments AS d
        ON e.department_id = d.id
)

SELECT
    employee_name,
    department_name,
    salary
FROM
    cte
WHERE
    rk <= 3
ORDER BY
    department_name ASC,
    salary DESC