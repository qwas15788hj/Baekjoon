from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        heap = []
        heappush(heap, [0, 0, 0])
        visited = [[1e9] * m for _ in range(n)]
        visited[0][0] = 0
        while heap:
            c, x, y = heappop(heap)
            if x == n-1 and y == m-1:
                return c
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    nc = max(c, abs(heights[x][y] - heights[nx][ny]))
                    if visited[nx][ny] > nc:
                        heappush(heap, [nc, nx, ny])
                        visited[nx][ny] = nc
        
        return -1