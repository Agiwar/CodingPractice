-- MySQL

SELECT 
    COUNT(DISTINCT
        LEAST(receiver_id, sender_id)
        , GREATEST(receiver_id, sender_id)
    ) AS total_conv_threads
FROM
    messenger_sends


-- PostgreSQL: No LEAST nor GREATEST

SELECT 
    COUNT(DISTINCT
        CASE WHEN receiver_id < sender_id THEN ROW(receiver_id, sender_id)
        ELSE ROW(sender_id, receiver_id)
        END
    ) AS total_conv_threads
FROM
    messenger_sends