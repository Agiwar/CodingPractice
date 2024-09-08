WITH cte AS (
    SELECT
        id,
        created_at,
        transaction_value,
        ROW_NUMBER() OVER(PARTITION BY DATE(created_at) ORDER BY created_at DESC) AS rk
    FROM
        bank_transactions
)

SELECT
    created_at,
    transaction_value,
    id
FROM
    cte
WHERE
    rk = 1
ORDER BY
    created_at