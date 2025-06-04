import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h+x)]

for i in range(x, h):
    for j in range(y, w):
        arr[i][j] -= arr[i-x][j-y]
        
for i in range(h):
    print(*arr[i][:w])