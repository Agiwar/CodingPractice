SELECT
    s.buyer_id AS buyer_id
FROM
    Sales AS s
INNER JOIN
    Product AS p
    ON s.product_id = p.product_id
WHERE
    p.product_name IN ('S8', 'iPhone')
GROUP BY
    s.buyer_id
HAVING
    SUM(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) = 0