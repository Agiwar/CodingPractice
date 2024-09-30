-- You are working as a Data Analyst for TikTok.
-- Some videos go viral suddenly after a period of time.

-- Your task is to find for each User_Id, 
-- the video (Video_Id) with the Maximum number of likes (Likes) per day (Date). 

-- Note that some users might have multiple videos in a day, 
-- and the result need to show only the first uploaded video in case of tie on likes count.


-- Video_Stats Example Input:
-- User_Id	Video_Id	Date	        Likes
-- 101	    VV567	    2022-10-01	    150
-- 101	    VV234	    2022-10-01	    80
-- 101	    VV890	    2022-10-01	    150
-- 102	    VV101	    2022-10-01	    300
-- 102	    VV111	    2022-10-01	    200
-- 101	    VV123	    2022-10-02	    100
-- 101	    VV456	    2022-10-02	    120
-- 102	    VV789	    2022-10-02	    500


WITH cte AS (
    SELECT
        User_Id,
        Video_Id,
        `Date`,
        Likes,
        DENSE_RANK() OVER(PARTITION BY User_Id, `Date` ORDER BY Likes DESC, Video_Id ASC) AS rk
    FROM
        Video_Stats
)

SELECT
    User_Id,
    Video_Id,
    `Date`,
    Likes
FROM
    cte
WHERE
    rk = 1