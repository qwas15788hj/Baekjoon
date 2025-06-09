import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# cctv 작동 함수
def check(x, y, dire):
    for d in dire:
        nx, ny = x, y
        while True:
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if arr[nx][ny] == 6:
                break
            if arr[nx][ny] == 0:
                visited[nx][ny] = True
            nx += dx[d]
            ny += dy[d]

cctv = [] # cctv 위치
dir = [] # 각 cctv 보는 방향 체크
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j])
            if arr[i][j] == 1:
                dir.append([[0], [1], [2], [3]])
            elif arr[i][j] == 2:
                dir.append([[0, 1], [2, 3]])
            elif arr[i][j] == 3:
                dir.append([[0, 3], [1, 3], [1, 2], [0, 2]])
            elif arr[i][j] == 4:
                dir.append([[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]])
            elif arr[i][j] == 5:
                dir.append([[0, 1, 2, 3]])

# cctv 모든 경우의 수 체크
answer = 1e9
pro = list(product(*dir))
for p in pro:
    visited = [[False] * m for _ in range(n)]
    for i in range(len(p)):
        check(cctv[i][0], cctv[i][1], p[i])

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and not visited[i][j]:
                count += 1

    answer = min(answer, count)

print(answer)