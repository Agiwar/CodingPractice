-- this question is asking how many unique conversations there are

-- for example
-- id,  receiver_id,    sender_id
-- 1,   1,              2
-- 2,   1,              2
-- 3,   2,              1
-- 4,   1,              2
-- 5,   2,              1

-- these 5 threads with id are all the same conversation, use combination of (sender_id, receiver_id) to be PK,
-- no matter 1 sends to 2, or 2 sends to 1, they are the same conversation

WITH unique_threads AS (
    SELECT
        (LEAST(receiver_id, sender_id), GREATEST(receiver_id, sender_id))
    FROM
        messenger_sends
    GROUP BY
        (LEAST(receiver_id, sender_id), GREATEST(receiver_id, sender_id))
)
SELECT
    COUNT(*) AS total_conv_threads 
FROM
    unique_threads