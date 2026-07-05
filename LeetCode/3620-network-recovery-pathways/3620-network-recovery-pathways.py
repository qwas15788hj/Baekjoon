from heapq import heappush, heappop

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # 최대 거리 측정
        n, m = len(online), 0
        for a, b, c in edges:
            m = max(m, c)
        
        # 그래프 생성
        arr = [[] for _ in range(n)]
        for a, b, c in edges:
            arr[a].append([b, c])
        
        # 최대 길이 간선으로 도달할 수 있는지 체크(우선순위 큐 bfs)
        def bfs(m):
            heap = []
            heappush(heap, [0, 0])
            visited = [float('inf')] * n
            visited[0] = 0
            while heap:
                d, x = heappop(heap)
                if x == n-1:
                    return True

                if visited[x] < d:
                    continue
                
                # 다음 이동 위치가
                # 방문길이보다 작고, k보다 작고, online이고, 최대 간선 기준인 m보다 클 때 => 이동 가능
                for nx, nd in arr[x]:
                    cost = d + nd
                    if visited[nx] > cost and cost <= k and online[nx] and nd >= m:
                        heappush(heap, [cost, nx])
                        visited[nx] = cost
            
            return False

        # 간선의 최대 길이 찾기 (이분탐색)
        answer = -1
        start, end = 0, m
        while start <= end:
            mid = (start + end)//2
            if bfs(mid):
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return answer