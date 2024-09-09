WITH cte AS (
    SELECT
        seller_id,
        DENSE_RANK() OVER(ORDER BY SUM(price) DESC) AS rk
    FROM
        Sales
    GROUP BY
        seller_id
)

SELECT
    seller_id
FROM
    cte
WHERE
    rk = 1