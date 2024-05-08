from collections import deque

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[0] * m for _ in range(n)]
queue.append([0, 0])
visited[0][0] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and visited[nx][ny] == 0:
            queue.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

answer = 1e9
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] != 0:
            answer = visited[i][j] + (n-1-i) + (m-1-j)
            break

if visited[-1][-1] != 0:
    answer = min(answer, visited[-1][-1])

if answer > t:
    print("Fail")
else:
    print(answer)