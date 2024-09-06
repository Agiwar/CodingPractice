-- solution 1: table join fo tilter which has O(N^2) time complexity (in worst case) if Person has N rows
DELETE p1
FROM
    Person AS p1
CROSS JOIN
    Person AS p2
WHERE
    p1.email = p2.email
    AND p1.id > p2.id


-- solution 2: use NOT IN to filter the rows we wanna delete, time complexity is O(N * log N) due to grouping,
--             but it may cause bad performance in some database engine especially there are many distinct values 
DELETE
FROM
    Person
WHERE id NOT IN (
    SELECT
        MIN(id)
    FROM
        Person
    GROUP BY
        email
)


-- solution 3: use window function to find out the rows we wanna delete, this also has O(N * log N) time complexity
DELETE
FROM
    Person
WHERE
    id IN (
        SELECT
            id
        FROM (
            SELECT
                id,
                ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) AS r
            FROM
                Person
        ) AS tmp
        WHERE
            r > 1
    )