WITH cte AS (
    SELECT
        user_id,
        created_at,
        product_id,
        quantity,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY created_at, id) AS rk
    FROM
        transactions
)

SELECT
    user_id,
    created_at,
    product_id,
    quantity
FROM
    cte
WHERE
    rk = 3
ORDER BY
    user_id ASC