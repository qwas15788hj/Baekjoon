import sys
input = sys.stdin.readline

v, e = map(int, input().split())
arr = [[1e9] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = 1e9
for i in range(1, v+1):
    for j in range(1, v+1):
        if i != j and arr[i][j] != 1e9 and arr[j][i] != 1e9:
            answer = min(answer, arr[i][j] + arr[j][i])

if answer == 1e9:
    print(-1)
else:
    print(answer)