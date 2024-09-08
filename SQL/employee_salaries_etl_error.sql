WITH cte AS (
    SELECT
        first_name,
        last_name,
        salary,
        ROW_NUMBER() OVER(PARTITION BY CONCAT(first_name, ' ', last_name) ORDER BY id DESC) AS curr
    FROM
        employees
)

SELECT
    first_name,
    last_name,
    salary
FROM
    cte
WHERE
    curr = 1