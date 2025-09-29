/* Write your T-SQL query statement below */
SELECT TOP 1 customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(customer_number) > 1
ORDER BY COUNT(customer_number) DESC
