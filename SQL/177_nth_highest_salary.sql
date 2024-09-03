CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary
      FROM (
          SELECT DISTINCT
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS r
          FROM
            Employee
      ) AS t
      WHERE r = N
  );
END