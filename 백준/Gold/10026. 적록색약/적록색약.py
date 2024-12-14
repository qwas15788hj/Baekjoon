import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < n and 0 <= my < n and arr[x][y] == arr[mx][my] and not visited[mx][my]:
                visited[mx][my] = True
                queue.append([mx, my])

answer = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

answer_rg = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer_rg += 1

print(answer, answer_rg)