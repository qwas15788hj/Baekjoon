import sys
input = sys.stdin.readline
from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append([a, s])

    queue = []
    heappush(queue, [0, c])
    visited = [1e9] * (n+1)
    visited[c] = 0
    while queue:
        d, x = heappop(queue)
        if visited[x] < d:
            continue
            
        for nx, nd in arr[x]:
            if visited[nx] > d + nd:
                visited[nx] = d + nd
                heappush(queue, [d+nd, nx])

    count, time = 0, 0
    for i in range(1, n+1):
        if visited[i] != 1e9:
            count += 1
            time = max(time, visited[i])

    print(count, time)