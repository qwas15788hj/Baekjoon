from heapq import heappush, heappop

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n, m = len(online), 0
        for a, b, c in edges:
            m = max(m, c)
        
        # 그래프 생성
        arr = [[] for _ in range(n)]
        for a, b, c in edges:
            arr[a].append([b, c])

        # 0 -> n-1까지 도달 가능한지 체크
        def bfs(m):
            heap = []
            heappush(heap, [0, 0])
            visited = [float('INF')] * n
            visited[0] = 0
            while heap:
                d, x = heappop(heap)
                if x == n-1:
                    return True

                if visited[x] < d:
                    continue
                
                # 다음 위치로 이동이 
                # 1. k이하 / 2. 방문한 곳보다 가까운 거리 / 3. online / 4. 다음 이동 거리가 m이상일 때 => 이동 가능
                for nx, nd in arr[x]:
                    if d+nd <= k and visited[nx] > d+nd and online[nx] and nd >= m:
                        heappush(heap, [d+nd, nx])
                        visited[nx] = d+nd
            
            return False
        
        # 이분탐색으로 최대 길이 찾기
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