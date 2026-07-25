from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    dist = [[1e9] * (n+1) for _ in range(n+1)]
    for p, q, c in fares:
        arr[p].append([q, c])
        arr[q].append([p, c])
        dist[p][q] = c
        dist[q][p] = c
    
    heap = []
    heappush(heap, [0, s])
    visited = [1e9] * (n+1)
    visited[s] = 0
    while heap:
        c, x = heappop(heap)
        if visited[x] < c:
            continue
        for nx, nc in arr[x]:
            cost = c + nc
            if visited[nx] > cost:
                visited[nx] = cost
                heappush(heap, [cost, nx])
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for z in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][z] + dist[z][j])
    
    answer = visited[a] + visited[b]
    for i in range(1, n+1):
        if i == s:
            continue
        answer = min(answer, visited[i] + dist[i][a] + dist[i][b])
    
    return answer