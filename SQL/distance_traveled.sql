SELECT
    u.name AS name,
    SUM(CASE WHEN r.distance IS NULL THEN 0 ELSE r.distance END) AS distance_traveled
FROM
    users AS u
LEFT JOIN
    rides AS r
    ON u.id = r.passenger_user_id
GROUP BY
    u.id
ORDER BY
    distance_traveled DESC