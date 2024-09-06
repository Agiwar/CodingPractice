-- solution 1: group by + count
WITH cte AS (
    SELECT
        email,
        count(email) AS ct
    FROM
        Person
    GROUP BY
        email
)
SELECT
    email AS Email
FROM
    cte
WHERE
    ct > 1

-- solution 2: having count
SELECT
    email AS Email
FROM
    Person
GROUP BY
    email
HAVING COUNT(email) > 1