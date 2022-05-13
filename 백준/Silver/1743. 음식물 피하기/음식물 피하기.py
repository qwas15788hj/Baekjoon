from collections import deque

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v, w):
    queue = deque()
    queue.append((v, w))
    arr[v][w] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
    return count

answer = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt = bfs(i, j)
            answer.append(cnt)

answer.sort()
print(answer[-1])