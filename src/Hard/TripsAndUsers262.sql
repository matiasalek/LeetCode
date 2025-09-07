SELECT request_at AS Day,
    ROUND(CAST (SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) AS FLOAT)/COUNT(*), 2) AS "Cancellation Rate"
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes') AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes')
AND request_at BETWEEN '2013-10-01' and '2013-10-03'
GROUP BY request_at
