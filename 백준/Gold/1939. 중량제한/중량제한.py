import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
start, end = map(int, input().split())

queue = []
heappush(queue, [-1e9, start])
visited = [-1] * (n+1)
visited[start] = 1e9
while queue:
    c, x = heappop(queue)
    c = -c
    if x == end:
        print(c)
        break
    if visited[x] > c:
        continue

    for nx, nc in arr[x]:
        nc = min(nc, c)
        if visited[nx] < nc:
            heappush(queue, [-nc, nx])
            visited[nx] = nc