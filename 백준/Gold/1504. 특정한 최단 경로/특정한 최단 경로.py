from heapq import heappush, heappop

n, e = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
u, v = map(int, input().split())

def dijkstra(s):
    heap = []
    heappush(heap, [0, s])
    visited = [1e9] * (n+1)
    visited[s] = 0
    while heap:
        c, x = heappop(heap)
        if visited[x] < c:
            continue
        for nx, nc in arr[x]:
            if visited[nx] > c + nc:
                visited[nx] = c + nc
                heappush(heap, [c + nc, nx])

    return visited

d1, du, dv = dijkstra(1), dijkstra(u), dijkstra(v)

r1 = d1[u] + du[v] + dv[n]
r2 = d1[v] + dv[u] + du[n]

if r1 >= 1e9 and r2 >= 1e9:
    print(-1)
elif r1 < 1e9 and r2 >= 1e9:
    print(r1)
elif r1 >= 1e9 and r2 < 1e9:
    print(r2)
else:
    print(min(r1, r2))