import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(a, b, c):
    queue = []
    heappush(queue, [0, a])
    visited = [1e9] * (n+1)
    visited[a] = 0
    while queue:
        d, p = heappop(queue)
        if p == b:
            break

        if visited[p] < d:
            continue

        for np, nd in arr[p]:
            if np != c and visited[np] > d + nd:
                heappush(queue, [d+nd, np])
                visited[np] = d + nd

    return visited


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
x, y, z = map(int, input().split())

xy = dijkstra(x, y, -1)[y]
yz = dijkstra(y, z, -1)[z]
xz = dijkstra(x, z, y)[z]

answer1 = -1
if xy != 1e9 and yz != 1e9:
    answer1 = xy + yz

answer2 = -1
if xz != 1e9:
    answer2 = xz

print(answer1, answer2)