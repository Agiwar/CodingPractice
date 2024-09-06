SELECT DISTINCT
    u.name AS customer_name
FROM
    transactions AS t
INNER JOIN
    users AS u
    ON t.user_id = u.id
WHERE
    YEAR(t.created_at) BETWEEN '2019' AND '2020'
GROUP BY
    u.name,
    YEAR(t.created_at)
HAVING
    COUNT(t.id) > 3