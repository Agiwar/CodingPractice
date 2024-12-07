-- calculate the minute difference between events by each user
WITH each_user_event_min_diff AS (
    SELECT
        created_at,
        user_id,
        event,
        TIMESTAMPDIFF(MINUTE, LAG(created_at, 1, created_at) OVER(PARTITION BY user_id ORDER BY created_at), created_at) AS min_diff
    FROM
        events
),
-- calculate the cumulative minute difference by each user
cumulative_min_diff AS (
    SELECT
        created_at,
        user_id,
        event,
        SUM(min_diff) OVER(PARTITION BY user_id ORDER BY created_at) AS cum_min_diff
    FROM
        each_user_event_min_diff
),
-- define the session time frame, e.g., 0~60, 61~120, 121~180, etc
group_same_session AS (
    SELECT
        created_at,
        user_id,
        event,
        CASE
            WHEN cum_min_diff % 60 = 0 AND cum_min_diff > 0 THEN FLOOR((cum_min_diff - 1) / 60) + 1
            ELSE FLOOR(cum_min_diff / 60) + 1
        END AS grp
    FROM
        cumulative_min_diff
)
-- use dense rank to assign the session id for each user if the events are in the same time frame
SELECT
    created_at,
    user_id,
    event,
    DENSE_RANK() OVER(PARTITION BY user_id ORDER BY grp) AS session_id
FROM
    group_same_session