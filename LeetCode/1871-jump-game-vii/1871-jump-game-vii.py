from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue = deque([])
        visited = [False] * (n)
        if s[0] == '0':
            queue.append(0)
            visited[0] = True
        
        prev = 0
        while queue:
            x = queue.popleft()
            if x == n-1:
                return True
        
            low = x + minJump
            high = min(x + maxJump, n-1)
            for nx in range(max(prev+1, low), high+1):
                if 0 <= nx < n and s[nx] == '0' and not visited[nx]:
                    queue.append(nx)
                    visited[nx] = True
            prev = max(prev, high)
        
        return False