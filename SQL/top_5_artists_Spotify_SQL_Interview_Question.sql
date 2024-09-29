-- This answer result will never match the official solution due to ORDER BY issue.


WITH popular_artists_with_songs_appearances AS (
    SELECT
        a.artist_name AS artist_name,
        COUNT(g.song_id) AS song_appearances,
        DENSE_RANK() OVER(ORDER BY COUNT(g.song_id) DESC) AS artist_rank
    FROM
        global_song_rank AS g
    INNER JOIN
        songs AS s
        ON g.song_id = s.song_id
    INNER JOIN
        artists AS a
        ON s.artist_id = a.artist_id
    WHERE
        g.rank <= 10
    GROUP BY
        a.artist_name
    ORDER BY
        song_appearances DESC
)

SELECT
    artist_name,
    artist_rank
FROM
    popular_artists_with_songs_appearances
WHERE
    artist_rank <= 5
ORDER BY
    artist_rank ASC,
    artist_name ASC