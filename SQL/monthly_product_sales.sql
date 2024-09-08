SELECT
    DATE(`month`) AS `month`,
    SUM(CASE WHEN product_id = 1 THEN amount_sold ELSE 0 END) AS `1`,
    SUM(CASE WHEN product_id = 2 THEN amount_sold ELSE 0 END) AS `2`,
    SUM(CASE WHEN product_id = 3 THEN amount_sold ELSE 0 END) AS `3`,
    SUM(CASE WHEN product_id = 4 THEN amount_sold ELSE 0 END) AS `4`
FROM
    monthly_sales
GROUP BY
    DATE(`month`)
ORDER BY
    `month`