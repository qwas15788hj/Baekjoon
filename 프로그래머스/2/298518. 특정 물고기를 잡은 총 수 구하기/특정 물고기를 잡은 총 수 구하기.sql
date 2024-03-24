-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO A
    JOIN FISH_NAME_INFO B
    ON A.FISH_TYPE = B.FISH_TYPE
WHERE B.FISH_NAME IN ("BASS", "SNAPPER")