/* Write your T-SQL query statement below */
SELECT max(salary) AS "SecondHighestSalary" 
FROM Employee e 
WHERE e.salary <> (SELECT max(salary) FROM Employee) ;
