WITH calculate_comment_count AS (
    SELECT
        u.id AS id
        , SUM(CASE WHEN c.body IS NULL THEN 0 ELSE 1 END) AS comment_count
    FROM
        users AS u
    LEFT JOIN
        comments AS c
        ON u.id = c.user_id
        AND TO_CHAR(c.created_at, 'YYYY-MM') = '2020-01'
    GROUP BY
        u.id
)

SELECT
    comment_count
    , COUNT(id) AS frequency
FROM
    calculate_comment_count
GROUP BY
    comment_count