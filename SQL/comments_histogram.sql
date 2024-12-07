-- directly filter out body is null and the comment date is not 2020-01
WITH user_has_comment AS (
    SELECT
        u.id AS user_id,
        SUM(CASE WHEN c.body IS NULL OR TO_CHAR(c.created_at, 'YYYY-MM') != '2020-01' THEN 0 ELSE 1 END) AS comment_count 
    FROM
        users AS u
    LEFT JOIN
        comments AS c
        ON u.id = c.user_id
    GROUP BY
        u.id
)
SELECT
    comment_count,
    COUNT(user_id) AS frequency
FROM
    user_has_comment
GROUP BY
    comment_count