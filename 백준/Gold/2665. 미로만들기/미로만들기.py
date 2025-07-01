import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

black = 0
for i in arr:
    black += i.count(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1e9
queue = deque()
visited = [[1e9] * n for _ in range(n)]
queue.append([0, 0, 0])
visited[0][0] = 0
while queue:
    x, y, c = queue.popleft()
    if x == n and y == n:
        continue

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1 and visited[nx][ny] > c:
                queue.append([nx, ny, c])
                visited[nx][ny] = c
            if arr[nx][ny] == 0 and visited[nx][ny] > c+1:
                queue.append([nx, ny, c+1])
                visited[nx][ny] = c+1

print(visited[-1][-1])