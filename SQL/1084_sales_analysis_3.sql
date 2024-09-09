SELECT
    p.product_id AS product_id,
    p.product_name AS product_name
FROM
    Sales AS s
INNER JOIN
    Product AS p
    ON s.product_id = p.product_id
GROUP BY
    s.product_id
HAVING
    SUM(CASE WHEN s.sale_date BETWEEN '2019-01-01' AND '2019-03-31' THEN 0 ELSE 1 END) = 0