from heapq import heappush, heappop

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int ,input().split())

heap = []
heappush(heap, [0, s])
dist = [1e9] * (n+1)
dist[s] = 0
visited = [0] * (n+1)
while heap:
    c, x = heappop(heap)
    if dist[x] < c:
        continue
    for nx, nc in arr[x]:
        if dist[nx] > c + nc:
            dist[nx] = c + nc
            visited[nx] = x
            heappush(heap, [c + nc, nx])

print(dist[e])
a = [e]
while True:
    e = visited[e]
    if e == 0:
        break
    a.append(e)

print(len(a))
print(*a[::-1])