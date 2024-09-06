-- find all unbanned users, and Trips table join unbanned users table, this will return all valid trips
-- too many CTEs usage, it may cause bad performance cuz it will need to scan whole table when this CTE called
WITH unbanned AS (
    SELECT
        users_id
    FROM
        Users
    WHERE
        banned = 'No'
),
valid_trips AS (
    SELECT
        CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END AS canceled,
        t.request_at AS `Day`
    FROM
        Trips AS t
    INNER JOIN
        unbanned AS u1
        ON t.client_id = u1.users_id
    INNER JOIN
        unbanned AS u2
        ON t.driver_id = u2.users_id
    WHERE
        t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)
SELECT
    `Day`,
    ROUND(SUM(canceled) / COUNT(canceled), 2) AS `Cancellation Rate`
FROM
    valid_trips
GROUP BY
    `Day`


-- optimized solution:
SELECT
    t.request_at AS `Day`,
    ROUND(SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS `Cancellation Rate`
FROM
    Trips AS t
INNER JOIN
    Users AS u1
    ON t.client_id = u1.users_id
    AND u1.banned = 'NO'
INNER JOIN
    Users AS u2
    ON t.driver_id = u2.users_id
    AND u2.banned = 'NO'
WHERE
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    t.request_at