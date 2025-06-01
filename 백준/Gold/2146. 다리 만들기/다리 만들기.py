import sys
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num = 0
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and board[i][j] == 0:
            queue = deque([(i, j)])
            num += 1
            board[i][j] = num
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and board[nx][ny] == 0:
                        queue.append((nx, ny))
                        board[nx][ny] = num

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            queue = deque([(i, j)])
            start = board[i][j]
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and (dist[nx][ny] == 0 or dist[x][y] + 1 < dist[nx][ny]):
                        queue.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
                    elif 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and board[nx][ny] != start:
                        answer = min(answer, dist[x][y])

print(answer)