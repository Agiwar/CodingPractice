CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    manager_id INT
);

-- Insert employees with hierarchical structure
INSERT INTO Employee (employee_id, employee_name, manager_id) VALUES
(1, 'A', 2), -- A is managed by B
(2, 'B', NULL), -- B has no manager
(3, 'C', 2), -- C is managed by B
(4, 'D', 3), -- D is managed by C
(5, 'E', 4); -- E is managed by D



-- We want to see each employee's managers by manager level
WITH RECURSIVE EmployeeManagers AS (
    -- base case
    SELECT
        employee_id,
        employee_name,
        manager_id,
        NULL::INT[] AS employee_managers_report_line_asc
    FROM
        Employee
    WHERE
        manager_id IS NULL
    
    UNION ALL

    -- normal case
    SELECT
        e.employee_id AS employee_id,
        e.employee_name AS employee_name,
        e.manager_id,
        em.employee_managers_report_line_asc || em.employee_id
    FROM
        Employee AS e
    INNER JOIN
        EmployeeManagers AS em
        ON e.manager_id = em.employee_id
)
SELECT
    employee_id,
    employee_name,
    employee_managers_report_line_asc
FROM
    EmployeeManagers
ORDER BY
    employee_id;


































WITH RECURSIVE ManagerHierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        NULL::INT[] AS employee_report_line_managers_asc
    FROM
        Employee
    WHERE
        manger_id IS NULL
    
    UNION ALL

    SELECT
        e.employee_id AS employee_id,
        e.employee_name AS employee_name,
        e.manager_id AS manager_id,
        m.employee_report_line_managers_asc || m.employee_id AS employee_report_line_managers_asc
    FROM
        Employee AS e
    INNER JOIN
        ManagerHierarchy AS m
        ON e.manager_id = m.employee_id
)
SELECT
    employee_id,
    employee_name,
    employee_report_line_managers_asc
FROM
    ManagerHierarchy
ORDER BY
    employee_id;



WITH RECURSIVE ManagerHierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        NULL::INT[] AS employee_report_line_managers_asc,
        1 AS level -- Starting at level 1
    FROM
        Employee
    WHERE
        manager_id IS NULL
    
    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        m.employee_report_line_managers_asc || m.employee_id,
        m.level + 1 -- Increment the level
    FROM
        Employee AS e
    INNER JOIN
        ManagerHierarchy AS m
        ON e.manager_id = m.employee_id
)
SELECT
    employee_id,
    employee_name,
    employee_report_line_managers_asc,
    level
FROM
    ManagerHierarchy
ORDER BY
    employee_id;