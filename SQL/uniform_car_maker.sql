-- Given a table of cars with columns id and make,
-- write a query that outputs a random manufacturer’s name with an equal probability of selecting any name.

-- solution 1: ORDER BY RANDOM

-- Time complexity analysis:
-- • GROUP BY has O(n) time, n is size of table.
-- • ORDER BY RANDOM():
--     1. Before sorting, need to assign a random number for each row, this has O(n) time.
--     2. ORDER BY has O(n * log n) time due to sorting.

-- So overall time complexity is O(n * log n).

SELECT
    make
FROM
    cars
GROUP BY
    make
ORDER BY
    RANDOM()
LIMIT 1;




-- solution 2: optimized using OFFSET

-- The optimized one shown below, the main idea is:
-- 1. Avoid sorting.
-- 2. Avoid assigning random number for each row.

-- Time complexity analysis:
-- • From CTE: GROUP BY to deduplicate records has O(n), n is size of table
-- • Main query:
--     1. Scan table has O(n) time.
--     2. COUNT() in sub-query has O(n) time.
--     3. OFFSET has O(k) time, k is the number of records we skipped
-- • For RANDOM(): Just do generating random number one time

-- Overall time complexity is O(n + k), for small k, it's approximately O(n) which is better than O(n * log n)


WITH deduplicate_cars AS (
    SELECT
        make
    FROM
        cars
    GROUP BY
        make
)
SELECT
    make
FROM
    deduplicate_cars
LIMIT 1
OFFSET FLOOR(RANDOM() * (SELECT COUNT(*) FROM deduplicate_cars));