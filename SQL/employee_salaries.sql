WITH big_department AS (
    SELECT
        AVG(CASE WHEN e.salary > 100000 THEN 1 ELSE 0 END) AS percentage_over_100k,
        d.name AS department_name,
        COUNT(e.id) AS number_of_employees
    FROM
        employees AS e
    INNER JOIN
        departments AS d
        ON e.department_id = d.id
    GROUP BY
        e.department_id
    HAVING
        COUNT(e.id) >= 10
    ORDER BY
        number_of_employees DESC
    LIMIT 3
)

SELECT * FROM big_department ORDER BY percentage_over_100k