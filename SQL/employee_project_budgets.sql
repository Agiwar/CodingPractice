WITH deduplicate_employee_projects AS (  -- use GROUP BY to deduplicate instead of DISTINCT
    SELECT
        project_id,
        employee_id
    FROM
        employee_projects
    GROUP BY
        project_id,
        employee_id
)
SELECT
    p.title,
    p.budget::NUMERIC / COUNT(d.employee_id)::NUMERIC AS budget_per_employee
FROM
    projects AS p
INNER JOIN
    deduplicate_employee_projects AS d
    ON p.id = d.project_id
GROUP BY                                -- each project by the budget
    p.title,
    p.budget
ORDER BY
    budget_per_employee DESC
LIMIT 5;