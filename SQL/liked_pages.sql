-- f.user_id != p.user_id doesn't work is cuz this condition join key only happens 
-- when f.friend_id = p.user_id, which represents each user's friends' pages liked, 
-- but this doesn't guarantee this user doesn't like that page 
-- (we don't know whether this user like that page which is liked by his friends), 
-- the like behavior of user's their friends has nothing to do with this user's like behavior 

SELECT
    f.user_id,
    p.page_id,
    COUNT(p.page_id) AS num_friend_likes
FROM
    friends AS f
LEFT JOIN
    page_likes AS p
    ON f.friend_id = p.user_id
    -- AND f.user_id != p.user_id
WHERE
    (f.user_id, p.page_id) 
    NOT IN (
        SELECT user_id, page_id
        FROM page_likes
        GROUP BY user_id, page_id
    )
GROUP BY
    f.user_id,
    p.page_id