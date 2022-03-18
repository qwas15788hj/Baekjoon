import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = [[0]*n for _ in range(n)]

x, y = 0, 0
num = n*n
arr[0][0] = num

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    for i in range(4):
        while True:
            x += dx[i]
            y += dy[i]
            if x >= n or x < 0 or y >= n or y < 0 or arr[x][y] != 0:
                x -= dx[i]
                y -= dy[i]
                break
            else:
                num -= 1
                arr[x][y] = num
    if num == 1:
        break

for i in arr:
    print(*i)
for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            print(i+1, j+1)
            break