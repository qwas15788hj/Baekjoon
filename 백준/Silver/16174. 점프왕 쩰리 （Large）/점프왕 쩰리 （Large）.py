from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
queue.append([0, 0])
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == n-1:
        continue

    nx, ny = x+arr[x][y], y+arr[x][y]
    if 0 <= nx < n and not visited[nx][y]:
        queue.append([nx, y])
        visited[nx][y] = True
    if 0 <= ny < n and not visited[x][ny]:
        queue.append([x, ny])
        visited[x][ny] = True

if visited[n-1][n-1]:
    print("HaruHaru")
else:
    print("Hing")