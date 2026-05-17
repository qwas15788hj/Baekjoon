from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([])
        visited = [False] * n
        queue.append(start)
        visited[start] = True

        while queue:
            x = queue.popleft()
            nx = x + arr[x]
            if 0 <= nx < n and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
            
            nx = x - arr[x]
            if 0 <= nx < n and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
        
        for i in range(n):
            if arr[i] == 0 and visited[i]:
                return True
        
        return False