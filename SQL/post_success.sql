SELECT
    DATE(created_at) AS dt,
    (SUM(CASE WHEN `action` = 'post_submit' THEN 1 ELSE 0 END) / COUNT(DISTINCT user_id)) AS post_success_rate
FROM
    events
WHERE
    DATE(created_at) BETWEEN '2020-01-01' AND '2020-01-31'
GROUP BY
    DATE(created_at)