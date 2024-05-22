from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
check = []

def bfs(x, y):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append([x, y])
    visited[x][y] = True
    check.append([x, y])

    while queue:
        nx, ny = queue.popleft()
        for i in range(8):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < n and 0 <= my < m and not visited[mx][my]:
                if arr[x][y] < arr[mx][my]:
                    return 0
                if arr[x][y] == arr[mx][my]:
                    queue.append([mx, my])
                    visited[mx][my] = True
                    check.append([mx, my])

    return 1

answer = 0
for i in range(n):
    for j in range(m):
        if [i, j] not in check:
            answer += bfs(i, j)

print(answer)