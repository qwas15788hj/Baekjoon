import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

time = 0
while queue:
    size = len(queue)
    for i in range(size):
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append([nx, ny])

    time += 1

flag = True
for i in arr:
    if i.count(0) != 0:
        flag = False

if flag:
    print(time - 1)
else:
    print(-1)