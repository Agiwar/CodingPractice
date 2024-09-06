SELECT
    e1.name AS Employee
FROM
    Employee AS e1
INNER JOIN
    Employee AS e2
    ON e1.managerId = e2.id  -- to see every employee's manager's information who has manager
WHERE
    e1.salary > e2.salary