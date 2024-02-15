from collections import deque

arr = [list(map(int, input().split())) for _ in range(5)]
num = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])
    while queue:
        nx, ny, nz = queue.popleft()
        if len(nz) == 6:
            num.add(nz)
        else:
            for i in range(4):
                mx = nx + dx[i]
                my = ny + dy[i]
                if 0 <= mx < 5 and 0 <= my < 5:
                    queue.append([mx, my, nz + str(arr[mx][my])])


for i in range(5):
    for j in range(5):
        bfs(i, j, str(arr[i][j]))

print(len(num))