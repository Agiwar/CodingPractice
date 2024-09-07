WITH cte AS (
    SELECT
        e.salary AS salary
    FROM
        projects AS p
    INNER JOIN
        employees AS e
        ON p.employee_id = e.id
    GROUP BY
        p.employee_id
    HAVING
        COUNT(p.End_dt) = 0
)

SELECT SUM(salary) AS total_slack_salary FROM cte