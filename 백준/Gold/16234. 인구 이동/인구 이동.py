from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, num, total, count):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = num
    total[num] = arr[x][y]
    count[num] = 1

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < n and 0 <= my < n and l <= abs(arr[nx][ny]-arr[mx][my]) <= r and visited[mx][my] == 0:
                queue.append([mx, my])
                visited[mx][my] = num
                total[num] += arr[mx][my]
                count[num] += 1


while True:
    visited = [[0]*n for _ in range(n)]
    num = 1
    total = dict()
    count = dict()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, visited, num, total, count)
                num += 1

    sub_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub_arr[i][j] = total[visited[i][j]]//count[visited[i][j]]

    if arr == sub_arr:
        break
    else:
        arr = sub_arr
        time += 1

print(time)