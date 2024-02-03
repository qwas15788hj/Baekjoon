from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

graph = [[] * m for _ in range(n)]
for i in range(n):
    for j in range(0, (m*3), 3):
        avg = sum(arr[i][j:j+3])
        if avg >= t * 3:
            avg = 255
        else:
            avg = 0

        graph[i].append(avg)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < n and 0 <= my < m and not visited[mx][my] and graph[mx][my] == 255:
                queue.append([mx, my])
                visited[mx][my] = True

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)