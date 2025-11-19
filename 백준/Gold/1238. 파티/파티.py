from heapq import heappush, heappop

def Dijkstra(start):
    queue = []
    heappush(queue, [0, start])
    visited = [1e9] * (n+1)
    visited[start] = 0
    while queue:
        c, p = heappop(queue)
        if visited[p] < c:
            continue

        for nx, nc in arr[p]:
            if visited[nx] > c + nc:
                visited[nx] = c + nc
                heappush(queue, [c + nc, nx])

    return visited

n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a].append([b, t])

answer = 0
check = Dijkstra(x)
for i in range(1, n+1):
    if i == x:
        continue
    answer = max(answer, check[i] + Dijkstra(i)[x])

print(answer)