-- Using the data from the video and user interactions on TikTok,
-- calculate the average, maximum, and minimum durations of videos watched by users, 
-- rounded to the nearest whole number. 

-- Additionally, calculate the square root of the total number of likes
-- given by users and present it as totalLikesSQRT. 

-- Assume we only have data for a single day.
-- Here are the data tables:


-- videos Example Input:
-- video_id	duration_secs
-- 001	    60
-- 002	    45
-- 003	    75
-- 004	    120
-- 005	    30


-- user_watched_videos Example Input:
-- user_id	video_id	watched_duration_secs
-- 123	    001	        60
-- 265	    002	        30
-- 362	    003	        55
-- 192	    004	        120
-- 981	    005	        25


-- user_likes Example Input:
-- user_id	video_id	liked
-- 123	    001	        TRUE
-- 265	    002	        FALSE
-- 362	    003	        TRUE
-- 192	    004	        TRUE
-- 981	    005	        TRUE



SELECT
    ROUND(AVG(t1.watched_duration_secs)) AS avg_watched_duration,
    MAX(t1.watched_duration_secs) AS max_watched_duration,
    MIN(t1.watched_duration_secs) AS min_watched_duration,
    SQRT(SUM(CASE WHEN t2.liked = 'TRUE' THEN 1 ELSE 0 END)) AS totalLikesSQRT
FROM
    user_watched_videos AS t1
INNER JOIN
    user_likes AS t2
    ON t1.user_id = t2.user_id
    AND t1.video_id = t2.video_id