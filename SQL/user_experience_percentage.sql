WITH cte AS (
    SELECT
        user_id,
        position_name,
        LEAD(position_name, 1) OVER(PARTITION BY user_id ORDER BY start_date) AS next_position
    FROM
        user_experiences
)
SELECT
    COUNT(DISTINCT user_id) / (SELECT COUNT(DISTINCT user_id) FROM cte) AS percentage
FROM
    cte
WHERE
    position_name = 'Data Analyst'
    AND next_position = 'Data Scientist'