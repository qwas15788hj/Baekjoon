# Write your MySQL query statement below
SELECT sub.person_name
FROM (
    SELECT a.person_name, SUM(b.weight) AS total
    FROM Queue a
    JOIN Queue b ON b.turn <= a.turn
    GROUP BY a.turn, a.person_name
) sub
WHERE sub.total <= 1000
ORDER BY sub.total DESC
LIMIT 1