SELECT
    u.name AS name,
    u.id AS user_id,
    ROUND(SUM(t.quantity * p.price), 2) AS total_cost
FROM
    transactions AS t
INNER JOIN
    products AS p
    ON t.product_id = p.id
INNER JOIN              -- it says by user ordered, not by each user
    users AS u
    ON t.user_id = u.id
GROUP BY
    u.id,
    u.name
ORDER BY
    total_cost DESC