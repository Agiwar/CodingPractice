WITH calculate_event_minute_diff AS (
    SELECT
        created_at
        , user_id
        , event
        , TIMESTAMPDIFF(
            MINUTE
            , LAG(created_at) OVER(PARTITION BY user_id ORDER BY created_at)
            , created_at
        ) AS minute_diff
    FROM
        events
)

, check_is_new_session AS (
    SELECT
        created_at
        , user_id
        , event
        , CASE WHEN minute_diff > 60 OR minute_diff IS NULL THEN 1 ELSE 0 END AS is_new_session
    FROM
        calculate_event_minute_diff
)

SELECT
    created_at
    , user_id
    , event
    , SUM(is_new_session) OVER(PARTITION BY user_id ORDER BY created_at) AS session_id
FROM
    check_is_new_session