SELECT
    YEAR(created_at) AS `year`,
    product_id,
    ROUND(AVG(quantity), 2) AS avg_quantity
FROM
    transactions
GROUP BY
    YEAR(created_at),
    product_id
ORDER BY
    `year`,
    product_id