-- This difficulty of this question is if there's no second highest salary, need to return NULL not empty record.


-- solution 1: intuitive but not so efficient due to NOT IN syntax
-- time = O(n) + O(n) ~= O(n)
SELECT
    MAX(salary) AS SecondHighestSalary
FROM
    Employee
WHERE
    salary NOT IN (SELECT MAX(salary) FROM Employee);


-- solution 2: dense_rank
-- time = O(n * log n) + O(n) ~= O(n * log n)
WITH ranking_salary AS (
    SELECT
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS r
    FROM
        Employee
)
SELECT 
    max(salary) AS SecondHighestSalary
FROM
    ranking_salary
WHERE
    r = 2;


-- solution 3: limit + offset
-- time = O(n * log n) + O(n) ~= O(n * log n)
SELECT (
    SELECT
        salary
    FROM
        Employee
    GROUP BY
        salary
    ORDER BY
        salary DESC
    LIMIT 1
    OFFSET 1
) AS SecondHighestSalary;


-- solution 4: limit + offset + case when
-- time = O(n) + O(n * log n) ~= O(n * log n)
SELECT
    CASE WHEN COUNT(*) = 1 THEN NULL ELSE MIN(salary) AS SecondHighestSalary
FROM (
    SELECT
        salary
    FROM
        Employee
    GROUP BY
        salary
    ORDER BY
        salary DESC
    LIMIT 2
) AS t;
