import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
queue = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            heappush(queue, [time, arr[i][j], i, j])

while time != s:
    size = len(queue)
    for _ in range(size):
        t, virus, nx, ny = heappop(queue)
        for k in range(4):
            mx = nx + dx[k]
            my = ny + dy[k]
            if 0 <= mx < n and 0 <= my < n and arr[mx][my] == 0:
                arr[mx][my] = virus
                heappush(queue, [time+1, virus, mx, my])

    time += 1

print(arr[x-1][y-1])