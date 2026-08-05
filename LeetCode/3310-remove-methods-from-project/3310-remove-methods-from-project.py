from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        arr = [[] for _ in range(n)]
        for a, b in invocations:
            arr[a].append(b)
        
        def bfs(s):
            queue = deque([s])
            visited = [False] * n
            visited[s] = True
            while queue:
                x = queue.popleft()
                for nx in arr[x]:
                    if not visited[nx]:
                        queue.append(nx)
                        visited[nx] = True
            
            return visited
        
        result = bfs(k) # k와 연결된 지워야하는 정점
        for a, b in invocations:
            if not result[a] and result[b]:
                return list(range(n))
        
        return [i for i in range(n) if not result[i]]