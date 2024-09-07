-- solution 1
WITH cte AS (
    SELECT
        m.name AS manager,
        COUNT(e.id) AS team_size
    FROM
        employees AS e
    INNER JOIN
        managers AS m
        ON e.manager_id = m.id
    GROUP BY
        e.manager_id
)

SELECT
    manager,
    team_size
FROM
    cte
WHERE
    team_size = (SELECT MAX(team_size) FROM cte)


-- solution 2
SELECT
    m.name AS manager,
    COUNT(e.id) AS team_size
FROM
    employees AS e
INNER JOIN
    managers AS m
    ON e.manager_id = m.id
GROUP BY
    e.manager_id
ORDER BY
    team_size DESC
LIMIT 1