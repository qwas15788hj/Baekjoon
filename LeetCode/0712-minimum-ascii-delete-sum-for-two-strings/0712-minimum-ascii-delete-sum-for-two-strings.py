class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        arr = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    arr[i][j] = arr[i-1][j-1] + ord(s1[i-1])
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        
        answer = 0
        for i in range(n):
            answer += ord(s1[i])
        for i in range(m):
            answer += ord(s2[i])
        
        return answer - arr[-1][-1]*2