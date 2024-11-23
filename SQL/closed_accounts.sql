WITH active_account AS (
    SELECT
        account_id
    FROM
        account_status
    WHERE
        date = '2019-12-31'
        AND status = 'open'
)

, inactive_account AS (
    SELECT
        account_id
    FROM
        account_status
    WHERE
        date = '2020-01-01'
        AND status = 'closed'
)

SELECT
    ROUND(
        (CAST(COUNT(a.account_id) AS NUMERIC) / 
        CAST((SELECT COUNT(account_id) FROM active_account) AS NUMERIC))
        , 2
    ) AS percentage_closed
FROM
    active_account AS a
INNER JOIN
    inactive_account AS i
    ON a.account_id = i.account_id