import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(s):
    queue = []
    heappush(queue, [0, s])
    visited = [1e9] * (n+1)
    visited[s] = 0
    prev = [-1] * (n+1)
    while queue:
        d, x = heappop(queue)

        if visited[x] < d:
            continue

        for nx, nd in arr[x]:
            if visited[nx] > d + nd:
                heappush(queue, [d+nd, nx])
                visited[nx] = d + nd
                if x == s:
                    prev[nx] = nx
                else:
                    prev[nx] = prev[x]

    return prev


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

answer = [[-1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    v = dijkstra(i)
    for j in range(1, n+1):
        if i != j:
            answer[i][j] = v[j]

for i in range(1, n+1):
    answer[i][i] = "-"
    print(*answer[i][1:])