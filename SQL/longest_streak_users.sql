-- Given a table with event logs, find the top five users with the longest continuous streak of visiting the platform.

-- Note: A continuous streak counts if the user visits the platform at least once per day on consecutive days.

-- Example:

-- Input:

-- events table
-- Column	    Type
-- user_id	    INTEGER
-- created_at	DATETIME
-- url	        VARCHAR


-- Output:
-- Column	        Type
-- user_id	        INTEGER
-- streak_length	INTEGER


-- just calculate the number of days which is consecutive, the number of visits each day doesn't matter

WITH record_each_user_per_day AS (
    SELECT
        user_id
        , DATE(created_at) AS visit_date
    FROM
        events
    GROUP BY
        user_id
        , DATE(created_at)
)

, group_day_diff AS (
    SELECT
        user_id
        ,visit_date - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY visit_date)::INT AS n_group
    FROM
        record_each_user_per_day
)

, user_who_is_consecutive AS (
    SELECT
        user_id
        , COUNT(n_group) AS streak_length_each_grp
    FROM
        group_day_diff
    GROUP BY
        user_id
        , n_group
)

SELECT
    user_id
    , MAX(streak_length_each_grp) AS streak_length
FROM
    user_who_is_consecutive
GROUP BY
    user_id
ORDER BY
    streak_length DESC
    , user_id ASC
LIMIT 5;