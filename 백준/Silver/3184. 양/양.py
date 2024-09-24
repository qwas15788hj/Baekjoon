from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if arr[i][j] == "#":
            visited[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_sheep, total_wolf = 0, 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != "#" and not visited[i][j]:
            sheep, wolf = 0, 0
            queue = deque([])
            queue.append([i, j])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                if arr[x][y] == "o":
                    sheep += 1
                if arr[x][y] == "v":
                    wolf += 1
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != "#" and not visited[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = True

            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)