from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    answer = [1e9, 1e9]
    
    arr = [[] for _ in range(n+1)]
    for a, b, c in paths:
        arr[a].append([b, c])
        arr[b].append([a, c])
    
    heap = []
    visited = [1e9] * (n+1)
    g_dic = dict()
    s_dic = dict()
    for g in gates:
        g_dic[g] = 1
        heappush(heap, [0, g])
        visited[g] = 0
    for s in summits:
        s_dic[s] = 1
    
    while heap:
        c, x = heappop(heap)
        if visited[x] < c:
            continue
            
        if x in s_dic:
            if answer[1] > c:
                answer = [x, c]
            elif answer[1] == c and answer[0] > x:
                answer = [x, c]
            continue
        
        for nx, nc in arr[x]:
            cost = max(c, nc)
            if visited[nx] > cost:
                visited[nx] = cost
                heappush(heap, [cost, nx])
    
    return answer