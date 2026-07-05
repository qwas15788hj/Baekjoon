from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        arr = [[] for _ in range(n+1)]
        for a, b, c in roads:
            arr[a].append([b, c])
            arr[b].append([a, c])

        queue = deque([1])
        visited = [False] * (n+1)
        visited[1] = True
        dic = dict()
        dic[1] = 1e9

        while queue:
            x = queue.popleft()
            for nx, nd in arr[x]:
                dic[1] = min(dic[1], nd)
                if not visited[nx]:
                    queue.append(nx)
                    visited[nx] = True
                    
        return dic[1]