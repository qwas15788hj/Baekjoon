from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for _ in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    queue = deque([])
                    queue.append([i, j])
                    visited[i][j] = True
                    cnt = 1
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                                queue.append([nx, ny])
                                visited[nx][ny] = True
                                cnt += 1
                    
                    answer = max(answer, cnt)
        
        return answer