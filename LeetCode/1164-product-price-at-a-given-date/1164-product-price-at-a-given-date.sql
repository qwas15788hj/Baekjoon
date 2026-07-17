# Write your MySQL query statement below
SELECT a.product_id, IFNULL(b.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) a
LEFT JOIN (
    SELECT product_id, new_price, change_date
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date) AS max_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) b
ON a.product_id = b.product_id