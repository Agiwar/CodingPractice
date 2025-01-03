-- Given a table of Facebook posts, for each user who posted at least twice in 2021, 
-- write a query to find the number of days between each user’s first post of the year and last post of the year in the year 2021. 
-- Output the user and number of the days between each user's first and last post.


-- posts Table:
-- user_id	    integer
-- post_id	    integer
-- post_content	text
-- post_date	timestamp


-- Example Output:
-- user_id	days_between
-- 151652	2
-- 661093	21


SELECT
    user_id,
    MAX(DATE(post_date)) - MIN(DATE(post_date)) AS days_between
FROM
    posts
WHERE
    TO_CHAR(post_date, 'YYYY') = '2021'
GROUP BY
    user_id
HAVING
    COUNT(post_id) >= 2;