/* Write your T-SQL query statement below */
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM PERSON
    GROUP BY email
);
