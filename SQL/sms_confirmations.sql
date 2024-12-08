-- Write a query to calculate the number of responses grouped by carrier and country to the SMSs sent by the system on February 28th, 2020.

-- User's response must happen when the confirmation msg is the last one for that user (once confirm, system won't send msg to the user anymore)


WITH find_confirmation_msg_seq AS (
    SELECT
        DATE(ds) AS ds,
        country,
        carrier,
        phone_number,
        ROW_NUMBER() OVER(PARTITION BY phone_number ORDER BY DATE(ds) DESC) AS r
    FROM
        sms_sends
    WHERE
        type = 'confirmation'
)
SELECT
    f.carrier AS carrier,
    f.country AS country,
    COUNT(c.phone_number) AS unique_numbers
FROM
    find_confirmation_msg_seq AS f
INNER JOIN
    confirmers AS c
    ON f.phone_number = c.phone_number
WHERE
    f.r = 1
    AND f.ds = '2020-02-28'
GROUP BY
    f.carrier,
    f.country
    