SELECT
    department,
    MAX(salary) AS largest_salary
FROM
    employees
GROUP BY
    department