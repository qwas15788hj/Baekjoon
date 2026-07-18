from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        queue = deque([])
        visited = [[0] * (1<<n) for _ in range(n)]
        for i in range(n):
            queue.append([i, 1<<i])
            visited[i][1<<i] = 1
        
        while queue:
            x, mask = queue.popleft()
            if mask == (1<<n)-1:
                return visited[x][mask] - 1
            
            for nx in graph[x]:
                nmask = mask | 1<<nx
                if not visited[nx][nmask]:
                    visited[nx][nmask] = visited[x][mask] + 1
                    queue.append([nx, nmask])