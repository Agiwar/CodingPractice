WITH cte AS (
    SELECT
        user_id
    FROM
        transactions
    GROUP BY
        user_id
    HAVING
        COUNT(DISTINCT DATE(created_at)) >= 2  -- different day
)
SELECT
    COUNT(*) AS num_of_upsold_customers
FROM
    cte