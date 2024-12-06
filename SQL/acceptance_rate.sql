SELECT
    ROUND(COUNT(r2.requester_id)::NUMERIC / COUNT(r1.requester_id)::NUMERIC, 4) AS acceptance_rate
FROM
    friend_requests AS r1
LEFT JOIN
    friend_accepts AS r2
    ON r1.requested_id = r2.acceptor_id