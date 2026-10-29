from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for _ in range(n)]
        answer = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    answer += 1
                    queue = deque([[i, j]])
                    visited[i][j] = True
                    while queue :
                        x, y = queue.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1':
                                queue.append([nx, ny])
                                visited[nx][ny] = True
        
        return answer