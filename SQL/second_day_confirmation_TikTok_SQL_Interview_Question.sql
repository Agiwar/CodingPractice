WITH cte AS (
    SELECT
        e.user_id AS user_id,
        t.signup_action AS signup_action,
        ROW_NUMBER() OVER(PARTITION BY e.user_id, e.email_id ORDER BY DATE(t.action_date) ASC) AS action_date_seq
    FROM
        emails AS e
    INNER JOIN
        texts AS t
        ON e.email_id = t.email_id
)

SELECT
    user_id
FROM
    cte
WHERE
    action_date_seq = 2
    AND signup_action = 'Confirmed'