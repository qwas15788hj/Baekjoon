import sys
input = sys.stdin.readline
from heapq import heappush, heappop
from collections import deque

# 최단거리 구하기
def dijkstra1(start):
    queue = []
    heappush(queue, [0, s])
    visited = [1e9] * (n + 1)
    visited[s] = 0

    check = []
    d_check = 1e9
    while queue:
        c, x = heappop(queue)
        if visited[x] < c:
            continue

        for nx, nc in arr[x]:
            if visited[nx] > c + nc:
                visited[nx] = c + nc
                parent[nx] = [x]
                heappush(queue, [c + nc, nx])
            elif visited[nx] == c + nc:
                parent[nx].append(x)

    return visited

# 역추적으로 최단거리 제거
def remove_edge(end):
    queue = deque([])
    queue.append(end)
    while queue:
        now = queue.popleft()
        for chd in parent[now]:
            if not remove[chd][now]:
                remove[chd][now] = True
                queue.append(chd)

# 역추적 후 최단거리 재측정
def dijkstra2(start):
    queue = []
    heappush(queue, [0, start])
    visited = [1e9] * (n+1)
    visited[start] = 0

    while queue:
        c, x = heappop(queue)
        if visited[x] < c:
            continue

        for nx, nc in arr[x]:
            if remove[x][nx]:
                continue

            if visited[nx] > c + nc:
                visited[nx] = c + nc
                heappush(queue, [c + nc, nx])

    return visited


while True:
    n, m = map(int, input().split())
    if n == 0 and m== 0:
        break
    s, d = map(int, input().split())
    arr = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        arr[u].append([v, p])

    remove = [[False] * n for _ in range(n)]
    parent = [[] for _ in range(n)]

    dist1 = dijkstra1(s)
    remove_edge(d)
    dist2 = dijkstra2(s)

    if dist2[d] == 1e9:
        print(-1)
    else:
        print(dist2[d])