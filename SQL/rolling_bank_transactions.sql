SELECT
    DATE_FORMAT(created_at, '%Y-%m-%d') AS dt,
    AVG(SUM(transaction_value)) OVER(ORDER BY DATE_FORMAT(created_at, '%Y-%m-%d') ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_three_day
FROM
    bank_transactions
WHERE
    transaction_value > 0
GROUP BY
    DATE(created_at)