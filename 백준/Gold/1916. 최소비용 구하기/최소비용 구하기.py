from heapq import heappush, heappop

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int, input().split())

queue = []
heappush(queue, [0, s])
visited = [1e9] * (n+1)
visited[s] = 0
while queue:
    c, x = heappop(queue)
    if visited[x] < c:
        continue
    for nx, nc in arr[x]:
        if visited[nx] > c + nc:
            visited[nx] = c + nc
            heappush(queue, [c + nc, nx])

print(visited[e])