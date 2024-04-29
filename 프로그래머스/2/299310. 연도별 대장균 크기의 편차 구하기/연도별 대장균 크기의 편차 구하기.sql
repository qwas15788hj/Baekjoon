-- 코드를 작성해주세요
SELECT B.YEAR, (MAX_SIZE - SIZE_OF_COLONY) AS YEAR_DEV, ID
FROM ECOLI_DATA A
    JOIN ( SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE, YEAR(DIFFERENTIATION_DATE) AS YEAR
            FROM ECOLI_DATA
            GROUP BY YEAR(DIFFERENTIATION_DATE) ) B
    ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY B.YEAR, YEAR_DEV