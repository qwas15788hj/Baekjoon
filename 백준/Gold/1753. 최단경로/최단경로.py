import sys
input = sys.stdin.readline
from heapq import heappush, heappop

v, e = map(int, input().split())
k = int(input())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

queue = []
heappush(queue, [0, k])
visited = [1e9] * (v+1)
visited[k] = 0
while queue:
    d, x = heappop(queue)
    if visited[x] < d:
        continue

    for nx, nd in arr[x]:
        if visited[nx] > d + nd:
            visited[nx] = d + nd
            heappush(queue, [d+nd, nx])

for i in range(1, v+1):
    if visited[i] == 1e9:
        print("INF")
    else:
        print(visited[i])