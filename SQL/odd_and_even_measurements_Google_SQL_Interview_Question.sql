WITH identify_measurement_seq AS (
    SELECT
        measurement_value,
        measurement_time,
        ROW_NUMBER() OVER(PARTITION BY DATE(measurement_time) ORDER BY measurement_time ASC) AS seq_number
    FROM
        measurements
)

SELECT
    DATE(measurement_time) AS measurement_day,
    SUM(CASE WHEN seq_number % 2 = 1 THEN measurement_value ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN seq_number % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM
    identify_measurement_seq
GROUP BY
    DATE(measurement_time)
ORDER BY
    measurement_day