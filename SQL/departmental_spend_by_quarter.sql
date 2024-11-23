WITH cte AS (
    SELECT
        CASE
            WHEN TO_CHAR(transaction_date, 'MM') IN ('01', '02', '03') THEN 'Q1'
            WHEN TO_CHAR(transaction_date, 'MM') IN ('04', '05', '06') THEN 'Q2'
            WHEN TO_CHAR(transaction_date, 'MM') IN ('07', '08', '09') THEN 'Q3'
            WHEN TO_CHAR(transaction_date, 'MM') IN ('10', '11', '12') THEN 'Q4'
        END AS quarter
        , department
        , amount
    FROM
        transactions
    WHERE
        TO_CHAR(transaction_date, 'YYYY') = '2023'
)

SELECT
    quarter
    , SUM(CASE WHEN department = 'IT' THEN amount ELSE 0 END) AS it_spending
    , SUM(CASE WHEN department = 'HR' THEN amount ELSE 0 END) AS hr_spending
    , SUM(CASE WHEN department = 'Marketing' THEN amount ELSE 0 END) AS marketing_spending
    , SUM(CASE WHEN department NOT IN ('IT', 'HR', 'Marketing') THEN amount ELSE 0 END) AS other_spending
FROM
    cte
GROUP BY
    quarter