-- calculate the second difference between events by each user
WITH event_time_diff_each_user AS (
    SELECT
        created_at,
        user_id,
        event,
        TIMESTAMPDIFF(SECOND, LAG(created_at, 1, created_at) OVER(PARTITION BY user_id ORDER BY created_at), created_at) AS event_sec_diff
    FROM
        events
),
-- calculate the cumulative second difference by each user
cumulate_event_time_diff AS (
    SELECT
        created_at,
        user_id,
        event,
        SUM(event_sec_diff) OVER(PARTITION BY user_id ORDER BY created_at) AS event_sec_diff_cum
    FROM
        event_time_diff_each_user
),
-- define the session time frame, e.g., 0~3600, 3601~7200, 7201~10800, etc
grouping_session_time_window AS (
    SELECT
        created_at,
        user_id,
        event,
        CASE
            WHEN event_sec_diff_cum > 0 AND event_sec_diff_cum % 3600 = 0 THEN FLOOR((event_sec_diff_cum - 1) / 3600) + 1
            ELSE FLOOR(event_sec_diff_cum / 3600) + 1
        END AS session_time_window
    FROM
        cumulate_event_time_diff
)
-- use dense rank to assign the session id for each user if the events are in the same time frame
SELECT
    created_at,
    user_id,
    event,
    DENSE_RANK() OVER(PARTITION BY user_id ORDER BY session_time_window) AS session_id
FROM
    grouping_session_time_window