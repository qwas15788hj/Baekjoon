-- 코드를 작성해주세요
SELECT A.ID, B.FISH_NAME, LENGTH
FROM FISH_INFO A
    JOIN FISH_NAME_INFO B
    ON A.FISH_TYPE = B.FISH_TYPE
WHERE (B.FISH_TYPE, LENGTH) IN ( SELECT B.FISH_TYPE, MAX(LENGTH)
                                FROM FISH_INFO A
                                JOIN FISH_NAME_INFO B
                                ON A.FISH_TYPE = B.FISH_TYPE
                                GROUP BY B.FISH_TYPE )
ORDER BY A.ID