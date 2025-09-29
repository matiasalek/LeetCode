/* Write your T-SQL query statement below */
SELECT user_id ,
ROUND(SUM(CASE WHEN activity_type='free_trial' THEN activity_duration END)*1.00 /COUNT(CASE WHEN activity_type='free_trial' THEN 1 END),2) AS trial_avg_duration
,ROUND(SUM(CASE WHEN activity_type='paid' THEN activity_duration END)*1.00/COUNT(CASE WHEN activity_type='paid' THEN 1 END),2) AS paid_avg_duration 
FROM UserActivity 
GROUP BY user_id 
HAVING COUNT(CASE WHEN activity_type='paid' THEN 1 END)>0
ORDER BY user_id ASC 
