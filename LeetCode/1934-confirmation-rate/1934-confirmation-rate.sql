-- # Write your MySQL query statement below
SELECT a.user_id,
    ROUND(IFNULL(SUM(CASE  
            WHEN b.action = 'confirmed' THEN 1
            ELSE 0
        end)/COUNT(b.action), 0), 2) AS confirmation_rate
FROM Signups a
LEFT JOIN Confirmations b
ON a.user_id = b.user_id
GROUP BY user_id