WITH cte1 AS (
    SELECT
        user_id,
        impression_id,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY dt DESC) AS curr,
        CASE WHEN impression_id = 'Bored' THEN 1 ELSE 0 END AS imp
    FROM
        ad_impressions
),

cte2 AS (
    SELECT
        user_id
    FROM
        cte1
    GROUP BY
        user_id
    HAVING
        SUM(imp) = 0
)

SELECT
    cte1.user_id AS user_id
FROM
    cte1
INNER JOIN
    cte2
    ON cte1.user_id = cte2.user_id
WHERE
    cte1.curr = 1
    AND cte1.impression_id = 'Excited'