import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[1e9] * m for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

shark = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            shark.append([i, j])

for i in range(len(shark)):
    x, y = shark[i][0], shark[i][1]
    queue = deque()
    queue.append([x, y])
    visited = [[0] * m for _ in range(n)]
    while queue:
        nx, ny = queue.popleft()
        for k in range(8):
            mx = nx + dx[k]
            my = ny + dy[k]
            if 0 <= mx < n and 0 <= my < m and visited[mx][my] == 0 and arr[mx][my] == 0:
                visited[mx][my] = visited[nx][ny] + 1
                queue.append([mx, my])

    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                dist[i][j] = min(visited[i][j], dist[i][j])

answer = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] != 1e9:
            answer = max(answer, dist[i][j])

print(answer)