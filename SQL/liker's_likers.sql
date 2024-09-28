SELECT
    t1.liker_id AS user,
    COUNT(DISTINCT t2.liker_id) AS `count`
FROM
    likes AS t1
INNER JOIN
    likes AS t2
    ON t1.liker_id = t2.user_id
GROUP BY
    t1.liker_id