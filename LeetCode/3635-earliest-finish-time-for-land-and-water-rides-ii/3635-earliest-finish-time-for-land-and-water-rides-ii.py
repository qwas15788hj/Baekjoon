class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        answer = 1e9
        land = []
        for i in range(n):
            land.append([landStartTime[i], landDuration[i]])
        land.sort(key=lambda x:(x[0] + x[1]))
        time = land[0][0] + land[0][1]
        for i in range(m):
            answer = min(answer, max(time, waterStartTime[i]) + waterDuration[i])

        water = []
        for i in range(m):
            water.append([waterStartTime[i], waterDuration[i]])
        water.sort(key=lambda x:(x[0] + x[1]))
        time = water[0][0] + water[0][1]
        for i in range(n):
            answer = min(answer, max(time, landStartTime[i]) + landDuration[i])

        return answer