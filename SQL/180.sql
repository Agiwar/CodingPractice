-- line 10 使用 distinct 是因為假設數字連續四個以上相同，則會有選取重複值的情況
WITH cte AS (
    SELECT
        num,
        LEAD(num, 1) OVER() AS next_num,
        LEAD(num, 2) OVER() AS next_next_num
    FROM
        Logs
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM
    cte
WHERE
    num = next_num
    AND next_num = next_next_num