from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        arr = [[] for _ in range(n+1)]
        for a, b, c in roads:
            arr[a].append([b, c])
            arr[b].append([a, c])
        
        visited = [0] * (n+1)
        dic = dict()
        for group in range(1, n+1):
            if visited[group] != 0:
                continue

            queue = deque([group])
            visited[group] = group
            dic[group] = 1e9
            while queue:
                x = queue.popleft()
                for nx, d in arr[x]:
                    dic[group] = min(dic[group], d)
                    if visited[nx] == 0:
                        queue.append(nx)
                        visited[nx] = group
        
        return dic[1]