from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited = [[[False] * (health+1) for _ in range(m)] for _ in range(n)]
        if grid[0][0] == 1:
            health -= 1
        queue = deque([[0, 0, health]])
        visited[0][0][health] = True
        
        while queue:
            x, y, h = queue.popleft()
            if x == n-1 and y == m-1:
                return True
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 0 and h > 0 and not visited[nx][ny][h]:
                        queue.append([nx, ny, h])
                        visited[nx][ny][h] = True
                    if grid[nx][ny] == 1 and (h-1) > 0 and not visited[nx][ny][h-1]:
                        queue.append([nx, ny, h-1])
                        visited[nx][ny][h-1] = True
        
        return False