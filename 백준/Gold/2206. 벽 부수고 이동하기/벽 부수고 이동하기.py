from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])
queue.append([0, 0, 0])
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
while queue:
    x, y, c = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == '0' and visited[nx][ny][c] == -1:
                queue.append([nx, ny, c])
                visited[nx][ny][c] = visited[x][y][c] + 1
            if arr[nx][ny] == '1' and c == 0:
                queue.append([nx, ny, 1])
                visited[nx][ny][1] = visited[x][y][0] + 1

answer = 1e9
for x in visited[-1][-1]:
    if x != -1:
        answer = min(answer, x)
if answer == 1e9:
    answer = -1
print(answer)