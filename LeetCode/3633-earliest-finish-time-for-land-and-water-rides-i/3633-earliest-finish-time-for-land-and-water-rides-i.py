class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        answer = 1e9
        for i in range(n):
            time = landStartTime[i] + landDuration[i]
            for j in range(m):
                result = max(time, waterStartTime[j]) + waterDuration[j]
                answer = min(answer, result)
        
        for j in range(m):
            time = waterStartTime[j] + waterDuration[j]
            for i in range(n):
                result = max(time, landStartTime[i]) + landDuration[i]
                answer = min(answer, result)

        return answer