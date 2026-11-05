class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n, m, answer = len(arr1), len(arr2), 0
        for i in range(n):
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
            else:
                answer += 1
        
        return answer