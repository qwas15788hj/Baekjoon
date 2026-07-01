from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque([[0, 0, 0]])
        visited = [[[-1] * (k+1) for _ in range(m)] for _ in range(n)]
        visited[0][0][0] = 0
        while queue:
            x, y, c = queue.popleft()
            if x == n-1 and y == m-1:
                return visited[x][y][c]
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 0 and visited[nx][ny][c] == -1:
                        queue.append([nx, ny, c])
                        visited[nx][ny][c] = visited[x][y][c] + 1
                    if grid[nx][ny] == 1 and (c+1) < (k+1) and visited[nx][ny][c+1] == -1:
                        queue.append([nx, ny, c+1])
                        visited[nx][ny][c+1] = visited[x][y][c] + 1
        
        return -1