SELECT
    CONCAT(first_name, ' ', last_name) AS employee_name
FROM
    employees AS e
LEFT JOIN
    managers AS m
    ON e.manager_id = m.id
WHERE
    e.manager_id IS NOT NULL
    AND e.join_date < m.join_date