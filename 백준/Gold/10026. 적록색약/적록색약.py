from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == arr[a][b]:
                queue.append([nx, ny])
                visited[nx][ny] = True

visited = [[False] * n for _ in range(n)]
answer1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer1 += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

visited = [[False] * n for _ in range(n)]
answer2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer2 += 1

print(answer1, answer2)