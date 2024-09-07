SELECT
    user_id,
    DATEDIFF(MAX(created_at), MIN(created_at)) AS no_of_days
FROM
    user_sessions
WHERE
    YEAR(created_at) = '2020'
GROUP BY
    user_id