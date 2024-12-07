-- Let’s say we have a table with an id and name fields. 
-- The table holds over 100 million rows and we want to sample a random row in the table without throttling the database.
-- Write a query to randomly sample a row from this table.


-- ORDER BY RANDOM() is an expensive operation especially for the large table, 
-- cuz it involves assigning the random number to each row, and sorting the entire rows, finally pick up the top result
SELECT
    id,
    name
FROM
    big_table
ORDER BY
    RANDOM()
LIMIT 1;


-- optimized
SELECT
    id,
    name
FROM
    big_table
OFFSET
    FLOOR(RANDOM() * (SELECT COUNT(*) FROM big_table))
LIMIT 1;