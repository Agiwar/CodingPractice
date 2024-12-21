-- Given a table with event logs, find the percentage of users that had at least one seven-day streak of visiting the same URL.

-- Note: Round the results to 2 decimal places. For example, if the result is 35.67% return 0.35.


-- Input:

-- events table

-- user_id	    INTEGER
-- created_at	DATETIME
-- url	        VARCHAR


-- output:

-- percent_of_users	FLOAT



-- Main idea: Use ROW_NUMBER() to generate incremental number to check whether or not the records are consecutive, the same url is the jey point.

-- solution:

WITH gen_incremental_seq AS (
    SELECT
        user_id,
        url,
        DATE(created_at) - (ROW_NUMBER() OVER(PARTITION BY user_id, url ORDER BY DATE(created_at)))::INT AS grp
    FROM
        events
),
user_has_seven_day_same_url AS (
    SELECT
        user_id,
        url,
        grp
    FROM
        gen_incremental_seq
    GROUP BY
        user_id,
        url,
        grp
    HAVING
        COUNT(*) >= 7
)
SELECT
    ROUND(COUNT(DISTINCT u.user_id)::NUMERIC / COUNT(DISTINCT e.user_id)::NUMERIC, 2) AS percent_of_users
FROM
    events AS e
LEFT JOIN
    user_has_seven_day_same_url AS u
    ON e.user_id = u.user_id