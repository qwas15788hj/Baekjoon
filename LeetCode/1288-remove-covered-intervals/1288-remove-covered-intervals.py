class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:(x[0], -x[1]))
        
        answer = 1
        x, y = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            if not (x <= intervals[i][0] and intervals[i][1] <= y):
                answer += 1
                x, y = intervals[i][0], intervals[i][1]

        return answer