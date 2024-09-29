-- But wait, did you get an activation rate of '0' when you ran the query? 
-- That's because dividing an integer with another integer would sometimes result in '0'.
-- To avoid this, we'll need to cast either the denominator or the numerator to DECIMAL type.

SELECT
    ROUND(SUM(CASE WHEN t.signup_action = 'Confirmed' THEN 1 ELSE 0 END)::DECIMAL / COUNT(*), 2) AS confirm_rate
FROM
    emails AS e
LEFT JOIN
    texts AS t
    ON e.email_id = t.email_id
WHERE
    t.email_id IS NOT NULL