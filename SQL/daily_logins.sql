WITH cte AS (
    SELECT
        user_id,
        COUNT(*) AS ct
    FROM
        user_logins
    WHERE
        DATE(login_date) = '2022-01-01'
    GROUP BY
        user_id
)

SELECT
    ct AS number_of_logins,
    COUNT(user_id) AS number_of_users
FROM
    cte
GROUP BY
    ct