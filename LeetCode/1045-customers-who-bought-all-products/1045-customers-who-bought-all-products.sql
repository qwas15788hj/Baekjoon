# Write your MySQL query statement below
SELECT sub.customer_id
FROM (
    SELECT customer_id, COUNT(DISTINCT product_key) AS cnt
    FROM Customer
    GROUP BY customer_id
) AS sub
WHERE sub.cnt = (SELECT COUNT(DISTINCT product_key) FROM Product) 