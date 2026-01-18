from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkAir(a, b):
    queue = deque([])
    queue.append([a, b])
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = True
                air[nx][ny] = True

answer = 0
while True:
    # 외부 공기 체크
    air = [[False] * m for _ in range(n)]
    checkAir(0, 0)

    # 녹는 치즈 체크
    cheese = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count = 0
                for k in range(4):
                    if air[i+dx[k]][j+dy[k]]:
                        count += 1
                if count >= 2:
                    cheese.append([i, j])

    if len(cheese) == 0:
        break

    for x, y in cheese:
        arr[x][y] = 0

    answer += 1

print(answer)