from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [[] for _ in range(n)]
        for a, b, c in flights:
            arr[a].append([b, c])
        
        queue = deque([[src, 0]])
        visited = [1e9] * n
        visited[src] = 0
        flag = 0
        while queue and flag <= k:
            size = len(queue)
            for _ in range(size):
                x, c = queue.popleft()
                for nx, nc in arr[x]:
                    cost = c + nc
                    if cost < visited[nx]:
                        queue.append([nx, cost])
                        visited[nx] = cost
            flag += 1
        
        if visited[dst] == 1e9:
            return -1
        else:
            return visited[dst]