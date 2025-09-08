/* Write your T-SQL query statement below */
SELECT pro.project_id,
ROUND(AVG(CAST(emp.experience_years AS DECIMAL(10, 2))), 2) AS average_years
FROM Project AS pro
LEFT JOIN Employee AS emp
ON pro.employee_id = emp.employee_id
GROUP BY pro.project_id
