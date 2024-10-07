-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A
    JOIN ( SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDERS
           FROM JULY
           GROUP BY FLAVOR) B
    ON A.FLAVOR = B.FLAVOR
ORDER BY TOTAL_ORDER + TOTAL_ORDERS DESC
LIMIT 3