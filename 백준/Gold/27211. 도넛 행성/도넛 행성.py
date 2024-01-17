from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        nx, ny = queue.popleft()
        for k in range(4):
            mx = nx + dx[k]
            my = ny + dy[k]
            if mx == -1:
                mx = n-1
            if mx == n:
                mx = 0
            if my == -1:
                my = m-1
            if my == m:
                my = 0

            if arr[mx][my] == 0 and not visited[mx][my]:
                queue.append([mx, my])
                visited[mx][my] = True

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)