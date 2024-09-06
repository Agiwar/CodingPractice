SELECT
    e.id AS employee_id
FROM
    projects AS p
INNER JOIN
    employees AS e
    ON p.employee_id = e.id
WHERE
    End_dt IS NOT NULL
GROUP BY
    p.employee_id
HAVING
    COUNT(p.project_id) >= 3
ORDER BY
    e.salary
LIMIT 5