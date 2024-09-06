-- Original solution: use LAG window function to find out the information of previous day of current date
--                    this will not work because this table doesn't guarantee there must be information of every day

-- WITH cte AS (
--     SELECT
--         id,
--         temperature,
--         LAG(temperature, 1) OVER(ORDER BY recordDate) AS temperature_yesterday
--     FROM
--         Weather
-- )
-- SELECT
--     id
-- FROM
--     cte
-- WHERE
--     temperature > temperature_yesterday


-- solution: use self join, and the join key is use DATEDIFF function to make sure
--           the temperature difference between yesterday and today

SELECT
    w2.id AS id
FROM
    Weather AS w1
INNER JOIN
    Weather AS w2
    ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE
    w2.temperature > w1.temperature