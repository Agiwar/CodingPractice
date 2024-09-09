SELECT
    p.item AS item,
    SUM(price) AS total_amount_spent
FROM
    purchases AS p
INNER JOIN
    users AS u
    ON p.user_id = u.user_id
WHERE
    YEAR(u.registration_date) = '2022'
GROUP BY
    p.item