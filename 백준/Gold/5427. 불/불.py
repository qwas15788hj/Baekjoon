import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    s_queue = deque()
    f_queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "@":
                s_queue.append([i, j])
            elif arr[i][j] == "*":
                f_queue.append([i, j])

    time = 0
    flag = False
    while s_queue:
        # 불 이동
        size = len(f_queue)
        for _ in range(size):
            x, y = f_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and (arr[nx][ny] == "." or arr[nx][ny] == "@"):
                    arr[nx][ny] = "*"
                    f_queue.append([nx, ny])

        # 상근 이동
        size = len(s_queue)
        for _ in range(size):
            x, y = s_queue.popleft()
            if x == 0 or x == n-1 or y == 0 or y == m-1:
                flag = True
                break

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == ".":
                    arr[nx][ny] = "@"
                    s_queue.append([nx, ny])

        time += 1

        if flag:
            break

    if flag:
        print(time)
    else:
        print("IMPOSSIBLE")