-- As a Data Analyst for TikTok, you've been asked to identify the users
-- who are the most active on the platform.

-- "Activity" in this context is defined by the number of videos a user uploads.
-- A "power user" is someone who has uploaded more than 1000 videos. 
-- Write a SQL query to list all of the power users,
-- sorted by the number of videos they have posted in descending order.


-- Users Example Input:
-- user_id	username	signup_date
-- 1	    user1	    01/01/2020
-- 2	    user2	    02/02/2020
-- 3	    user3	    05/05/2020
-- 4	    user4	    12/12/2020

-- Videos Example Input:
-- video_id	user_id	upload_date
-- 1001	    1	    01/02/2020
-- 1002	    1	    01/03/2020
-- 1003	    2	    02/03/2020
-- 1004	    3	    03/03/2020
-- 1005	    4	    04/04/2020
-- 1006	    4	    05/04/2020
-- 1007	    4	    05/04/2020
-- 1008	    4	    05/04/2020
-- 1009	    3	    06/04/2020
-- 1010	    2	    07/07/2020

SELECT
    u.username AS username,
    COUNT(v.video_id) AS num_videos
FROM
    Videos AS v
INNER JOIN
    Users AS u
    ON v.user_id = u.user_id
GROUP BY
    v.user_id
HAVING
    COUNT(v.video_id) > 1000
ORDER BY
    num_videos DESC