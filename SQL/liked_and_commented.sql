-- You’re given two tables, users and events.
-- The events table holds values of all of the user events in the action column (‘like’, ‘comment’, or ‘post’).

-- Write a query to get the percentage of users that have never liked or commented. Round to two decimal places.


-- Input:

-- users table
-- id	        INTEGER
-- name	        VARCHAR
-- created_at	DATETIME

-- events table
-- user_id	    INTEGER
-- action	    VARCHAR
-- created_at	DATETIME

-- Output:
-- percent_never	FLOAT


-- Main idea: Find out all users who have liked or commented, and then take all users to do LEFT JOIN

-- solution 1:
-- time: O(n + m), n is all users, m is users who likes or comments
-- space: O(n - m), cuz we want the users who never liked or commented
WITH user_like_or_comment AS (
    SELECT
        user_id
    FROM
        events
    WHERE
        action IN ('like', 'comment')
    GROUP BY
        user_id
)
SELECT
    ROUND(AVG(CASE WHEN u2.user_id IS NULL THEN 1 ELSE 0 END), 2) AS percent_never
FROM
    users AS u1
LEFT JOIN
    user_like_or_comment AS u2
    ON u1.id = u2.user_id