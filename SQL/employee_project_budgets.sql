SELECT
    p.title AS title,
    p.budget / COUNT(e.employee_id) AS budget_per_employee
FROM
    projects AS p
INNER JOIN
    employee_projects AS e
    ON p.id = e.project_id
GROUP BY
    p.id
ORDER BY
    budget_per_employee DESC
LIMIT 5