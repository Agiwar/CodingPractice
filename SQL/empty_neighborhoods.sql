SELECT
    n.name AS name
FROM
    neighborhoods AS n
LEFT JOIN
    users AS u
    ON n.id = u.neighborhood_id
GROUP BY
    n.id
HAVING
    COUNT(u.id) = 0