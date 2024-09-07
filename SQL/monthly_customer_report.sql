SELECT
    MONTH(t.created_at) AS `month`,
    COUNT(DISTINCT t.user_id) AS num_customers,
    COUNT(t.id) AS num_orders,
    SUM(t.quantity * p.price) AS order_amt  -- total amount = quantity * price
FROM
    transactions AS t
INNER JOIN
    products AS p
    ON t.product_id = p.id
WHERE
    YEAR(t.created_at) = '2020'
GROUP BY
    MONTH(t.created_at)
ORDER BY
    `month`