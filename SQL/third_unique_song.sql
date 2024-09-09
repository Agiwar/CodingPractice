WITH user_song_played_first_time AS (
    SELECT
        user_id,
        song_name,
        MIN(date_played) AS each_song_played_first_time
    FROM
        song_plays
    GROUP BY
        user_id,
        song_name
),

user_each_song_played_order AS (
    SELECT
        user_id,
        song_name,
        each_song_played_first_time,
        ROW_NUMBER() OVER(PARTITION BY user_id  ORDER BY each_song_played_first_time) AS song_played_order
    FROM
        user_song_played_first_time
),

user_third_song AS (
    SELECT
        user_id,
        song_name,
        each_song_played_first_time AS date_played 
    FROM
        user_each_song_played_order
    WHERE
        song_played_order = 3
)

SELECT
    u.name AS name,
    cte.date_played AS date_played,
    cte.song_name AS song_name
FROM
    users AS u
LEFT JOIN
    user_third_song AS cte
    ON u.id = cte.user_id