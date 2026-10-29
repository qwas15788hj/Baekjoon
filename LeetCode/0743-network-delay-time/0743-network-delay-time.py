from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        arr = [[] for _ in range(n+1)]
        for a, b, c in times:
            arr[a].append([b, c])
        
        heap = []
        visited = [1e9] * (n+1)
        heappush(heap, [0, k])
        visited[k] = 0
        while heap:
            c, x = heappop(heap)
            if visited[x] < c:
                continue
            for nx, nc in arr[x]:
                if visited[nx] > c + nc:
                    visited[nx] = c + nc
                    heappush(heap, [c + nc, nx])
        
        answer = -1
        for i in range(1, n+1):
            answer = max(answer, visited[i])
        
        if answer == 1e9:
            answer = -1

        return answer