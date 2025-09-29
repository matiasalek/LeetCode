/* Write your T-SQL query statement below */
/* 
1. Comprobar si la operation es Buy o Sell
1.1 Si es buy, SUM(price)
*/
SELECT stock_name, 
SUM(
    CASE WHEN operation = 'Sell' THEN price
    WHEN operation = 'Buy' THEN -price
    END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
