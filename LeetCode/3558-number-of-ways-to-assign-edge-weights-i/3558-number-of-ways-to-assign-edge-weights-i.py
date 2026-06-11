from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = 0
        for edge in edges:
            n = max(n, max(edge))

        arr = [[] for _ in range(n+1)]
        for a, b in edges:
            arr[a].append(b)
            arr[b].append(a)
        
        queue = deque([])
        queue.append(1)
        visited = [-1] * (n+1)
        visited[1] = 0
        while queue:
            x = queue.popleft()
            for nx in arr[x]:
                if visited[nx] == -1:
                    queue.append(nx)
                    visited[nx] = visited[x] + 1
        
        deep = max(visited)
        print(visited)
        return (2**(deep-1))%1000000007