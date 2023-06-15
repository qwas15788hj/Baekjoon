from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
queue = deque()
visited = [[False]*m for _ in range(n)]
count = 0
flag = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            flag = True
            queue.append([i, j])
            visited[i][j] = True
            break
    if flag:
        break

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != "X" and not visited[nx][ny]:
            queue.append([nx, ny])
            visited[nx][ny] = True
            if arr[nx][ny] == "P":
                count += 1

if count == 0:
    print("TT")
else:
    print(count)