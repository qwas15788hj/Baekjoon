from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
visited = [[False] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            answer += 1
            queue = deque([])
            queue.append([i, j])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for k in range(8):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = True

print(answer)