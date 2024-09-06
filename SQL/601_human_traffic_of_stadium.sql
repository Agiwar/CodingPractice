WITH cte AS (
    SELECT
        *,
        ROW_NUMBER() OVER(ORDER BY id) AS n,
        id - (ROW_NUMBER() OVER(ORDER BY id)) AS n_group
    FROM
        Stadium
    WHERE
        people >= 100
)
SELECT
    id,
    visit_date,
    people
FROM
    cte
WHERE
    n_group IN (
        SELECT
            n_group
        FROM
            cte
        GROUP BY
            n_group
        HAVING
            COUNT(n_group) >= 3
    )
ORDER BY
    visit_date