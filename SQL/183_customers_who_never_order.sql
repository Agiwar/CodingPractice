-- solution 1: using sybquery in where 
SELECT
    name AS Customers
FROM
    Customers
WHERE
    id NOT IN (
        SELECT
            customerId
        FROM
            Orders
    )


-- solution 2: Use left join to find out the nullable rows which mean that person has no order.
SELECT
    c.name AS Customers
FROM
    Customers AS c
LEFT JOIN
    Orders AS o
    ON c.id = o.customerId
WHERE
    o.id IS NULL


-- solution 3: use having count to explicitly show how many orders does each customer have
SELECT
    c.name AS Customers
FROM
    Customers AS c
LEFT JOIN
    Orders AS o
    ON c.id = o.customerId
GROUP BY
    c.id
HAVING
    COUNT(o.id) = 0