from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        answer = 0
        n = len(grid)
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        queue = deque([])
        visited = [[-1] * n for _ in range(n)]
        if grid[0][0] == 0:
            queue.append([0, 0])
            visited[0][0] = 1
        
        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == n-1:
                break
                
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == -1:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
        
        return visited[-1][-1]