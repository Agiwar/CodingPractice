-- solution 1: LEFT JOIN to find out all NULL records
-- time = O(n * k), n is size of Visits, k is size of Transactions (cuz not sorted or indexing, so it's not O(n + k))
SELECT
    v.customer_id AS customer_id,
    COUNT(v.customer_id) AS count_no_trans
FROM
    Visits AS v
LEFT JOIN
    Transactions AS t
    ON v.visit_id = t.visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id;


-- solution 2: NOT EXISTS return visit_id exists in Visits but not in Transactions
-- time = O(n * k)
SELECT
    v.customer_id AS customer_id,
    COUNT(v.customer_id) AS count_no_trans
FROM
    Visits AS v
WHERE NOT EXISTS (
    SELECT
        t.visit_id
    FROM
        Transactions AS t
    WHERE
        v.visit_id = t.visit_id
)
GROUP BY
    v.customer_id;


-- solution 3: If the goal is purely to count the unmatched rows, use a subquery instead of a join:
SELECT
    customer_id AS customer_id,
    COUNT(customer_id) AS count_no_trans
FROM
    Visits
WHERE
    visit_id NOT IN (
        SELECT
            visit_id
        FROM
            Transactions
        GROUP BY
            visit_id
    )
GROUP BY
    customer_id;


-- solution 4: use ALL
SELECT
    customer_id,
    COUNT(customer_id) AS count_no_trans
FROM
    Visits
WHERE
    visit_id != ALL(
        SELECT
            visit_id
        FROM
            Transactions
        GROUP BY
            visit_id
    )
GROUP BY
    customer_id;