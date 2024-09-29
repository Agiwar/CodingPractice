-- You have been given access to the TikTok database and you are tasked with the following:

-- TikTok has two primary tables: Users and Videos.
-- Each row in the Users table represents a unique user on the platform,
-- while each row in the Videos table represents a unique video that has been uploaded on the platform.
-- A video can be uploaded by a user, and the same user can 'like' or 'share' other videos, including their own.

-- Write a SQL query that shows the top 5 Users who have uploaded the videos that have received the most 'likes'. 
-- The output should display the User ID, the total number of videos they have uploaded, and the total number of 'likes' their videos have collectively received.

-- The two tables are structured as follows:

-- Users Example Input:
-- user_id	username	country     join_date
-- 1	    'user1'	    'USA'	    '2021-01-01'
-- 2	    'user2'	    'Canada'    '2021-02-01'
-- 3	    'user3'	    'UK'	    '2021-01-31'
-- 4	    'user4'	    'USA'	    '2021-01-30'
-- 5	    'user5'	    'Canada'    '2021-01-15'


-- Videos Example Input:
-- video_id	    upload_date	    user_id	    video_likes
-- 101	        '2021-01-01'	1	        500
-- 102	        '2021-02-01'	2	        1000
-- 103	        '2021-02-01'	1	        1500
-- 104	        '2021-03-01'	3	        2000
-- 105	        '2021-03-01'	4	        250
-- 106	        '2021-04-01'	5	        5000



SELECT
    u.user_id AS user_id,
    COUNT(v.video_id) AS total_videos,
    SUM(v.video_likes) AS total_likes
FROM
    Users AS u
INNER JOIN
    Videos AS v
    ON u.user_id = v.user_id
GROUP BY
    u.user_id
ORDER BY
    total_likes DESC
LIMIT 5