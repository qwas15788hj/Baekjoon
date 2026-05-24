from collections import deque

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        # 각 인덱스가 방문할 수 있는 곳 체크
        visited = [[] for _ in range(n)]
        for idx in range(n):
            for left in range(idx-1, idx-d-1, -1):
                if left < 0:
                    continue
                if arr[idx] > arr[left]:
                    visited[idx].append(left)
                else:
                    break
        
            for right in range(idx+1, idx+d+1):
                if right >= n:
                    continue
                if arr[idx] > arr[right]:
                    visited[idx].append(right)
                else:
                    break

        dp = [-1] * n
        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            dp[i] = 1
            for j in visited[i]:
                dp[i] = max(dp[i], 1 + dfs(j))
            return dp[i]
        
        answer = 0
        for i in range(n):
            answer = max(answer, dfs(i))
        
        return answer