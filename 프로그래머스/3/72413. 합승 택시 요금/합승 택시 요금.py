from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    dist = [[1e9] * (n+1) for _ in range(n+1)]
    for c, d, f in fares:
        arr[c].append([d, f])
        arr[d].append([c, f])
        dist[c][d] = f
        dist[d][c] = f
    
    # S부터 각 지점까지 거리 (다익스트라)
    heap = []
    heappush(heap, [0, s])
    visited = [1e9] * (n+1)
    visited[s] = 0
    while heap:
        cost, x = heappop(heap)
        if visited[x] < cost:
            continue
        for nx, nc in arr[x]:
            ncost = cost + nc
            if visited[nx] > ncost:
                heappush(heap, [ncost, nx])
                visited[nx] = ncost
    
    # 각 지점 별 거리 (플로이드 워셜)
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    answer = visited[a] + visited[b]
    for i in range(1, n+1):
        if i == s:
            continue
        answer = min(answer, visited[i] + dist[i][a] + dist[i][b])
    
    return answer