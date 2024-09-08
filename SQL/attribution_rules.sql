SELECT
    u.user_id AS user_id,
    CASE 
        WHEN SUM(CASE WHEN a.channel IN ('Facebook', 'Google') THEN 1 ELSE 0 END) >= 1 THEN 'paid'
        ELSE 'organic'
    END AS attribute
FROM
    user_sessions AS u
INNER JOIN
    attribution AS a
    ON u.session_id = a.session_id
GROUP BY
    u.user_id