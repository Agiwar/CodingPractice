WITH cte AS (
    SELECT
        id,
        recordDate,
        temperature,
        LEAD(temperature) OVER() AS next_temperature
    FROM
        Weather
)
