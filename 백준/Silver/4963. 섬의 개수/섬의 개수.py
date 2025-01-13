import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        nx, ny = queue.popleft()
        for k in range(8):
            mx = nx + dx[k]
            my = ny + dy[k]
            if 0 <= mx < h and 0 <= my < w and arr[mx][my] == 1 and not visited[mx][my]:
                queue.append([mx, my])
                visited[mx][my] = True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)