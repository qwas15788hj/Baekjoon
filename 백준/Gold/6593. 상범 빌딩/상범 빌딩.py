import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    arr = []
    for i in range(l):
        arr.append([list(input()) for _ in range(r)])
        temp = input()
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]

    queue = deque()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == "S":
                    queue.append([i, j, k, 0])
                    visited[i][j][k] = True

    flag = False
    answer = 0
    while queue:
        z, x, y, d = queue.popleft()
        if arr[z][x][y] == "E":
            flag = True
            answer = d
            break

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny]:
                if arr[nz][nx][ny] != "#":
                    queue.append([nz, nx, ny, d+1])
                    visited[nz][nx][ny] = True

    if flag:
        print(f'Escaped in {d} minute(s).')
    else:
        print("Trapped!")