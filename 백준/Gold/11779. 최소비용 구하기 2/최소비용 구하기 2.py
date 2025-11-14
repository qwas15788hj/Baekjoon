import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int, input().split())

queue = []
heappush(queue, [0, s, [s]])
visited = [1e9] * (n+1)
visited[s] = 0

check = []
while queue:
    d, x, v = heappop(queue)
    if visited[x] < d:
        continue
    if x == e:
        check = v
    for nx, nd in arr[x]:
        if visited[nx] > d + nd:
            visited[nx] = d + nd
            heappush(queue, [d + nd, nx, v + [nx]])

print(visited[e])
print(len(check))
print(*check)