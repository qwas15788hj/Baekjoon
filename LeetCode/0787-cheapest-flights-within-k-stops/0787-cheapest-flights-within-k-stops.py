from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [[] for _ in range(n)]
        for a, b, c in flights:
            arr[a].append([b, c])
        
        heap = []
        heappush(heap, [0, src, 0])
        visited = [1e9] * (n) # 해당 노드에 몇 번의 경유가 있었는지 체크
        while heap:
            cost, x, cnt = heappop(heap)
            if x == dst:
                return cost
            
            if cnt >= visited[x]:
                continue
            
            visited[x] = cnt
            if cnt > k:
                continue
            
            for nx, nc in arr[x]:
                heappush(heap, [cost+nc, nx, cnt+1])
        
        return -1