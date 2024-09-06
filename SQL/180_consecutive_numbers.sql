WITH cte AS (
    SELECT
        num,
        LEAD(num, 1) OVER() AS next_num,
        LEAD(num, 2) OVER() AS next_next_num
    FROM
        Logs
)
-- Using DISTINCT is because the same consecutive number may happen in different row
SELECT DISTINCT
    num AS ConsecutiveNums
FROM
    cte
WHERE
    num = next_num
    AND next_num = next_next_num