import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [[1] * m for _ in range(n)]
x, y = 0, 0
if k != 0:
    x = (k-1)//m
    y = (k-1)%m

for i in range(1, x+1):
    for j in range(1, y+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for i in range(x+1, n):
    arr[i][y] = 1
for i in range(y+1, m):
    arr[x][i] = 1

for i in range(x+1, n):
    for j in range(y+1, m):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[x][y] * arr[-1][-1])