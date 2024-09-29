-- On TikTok, each user can post several videos.
-- For business decisions, it's often necessary to know the average duration of these videos
-- to better understand the user engagement. 

-- For instance, if the average video duration is short, 
-- it could indicate that users on the platform prefer shorter, more concise content. 
-- Alternatively, longer average video lengths could infer that 
-- users enjoy or are more engaged with longer-form content. 

-- Calculate the average video duration for each TikTok user using the provided database tables.

-- Provided below is a snapshot of your 'users' table and 'videos' table:

-- users Example Input:
-- user_id	username	signup_date
-- 101	    user1	    06/01/2020
-- 102	    user2	    06/03/2020
-- 103	    user3	    06/05/2020


-- videos Example Input:
-- video_id	user_id	upload_date	video_length_seconds
-- 201	    101	    06/08/2022	60
-- 202	    101	    06/10/2022	120
-- 203	    102	    06/18/2022	90
-- 204	    103	    07/26/2022	100
-- 205	    103	    07/05/2022	120



-- calculate each user's average video duration 
-- >> use LEFT JOIN (cuz there may be users who don't have any videos uploaded)
SELECT
    u.username AS username,
    AVG(CASE WHEN v.video_length_seconds::DECIMAL IS NULL THEN 0 ELSE v.video_length_seconds) AS avg_video_length_seconds
FROM
    users AS u
LEFT JOIN
    videos AS v
    ON u.user_id = v.user_id
GROUP BY
    u.user_id