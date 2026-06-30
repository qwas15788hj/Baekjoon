from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([])
        visited = [[0] * (1 << n) for _ in range(n)]

        for i in range(n):
            queue.append([i, 1 << i])
            visited[i][1 << i] = True
        
        while queue:
            x, b = queue.popleft()
            if b == (1 << n) - 1:
                return visited[x][b] - 1
            
            for nx in graph[x]:
                nb = b | (1 << nx)
                if visited[nx][nb] == 0:
                    queue.append([nx, nb])
                    visited[nx][nb] = visited[x][b] + 1