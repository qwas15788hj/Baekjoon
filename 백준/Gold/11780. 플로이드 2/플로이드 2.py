n = int(input())
m = int(input())
arr = [[1e9] * (n+1) for _ in range(n+1)]
visited = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a][b] > c:
        arr[a][b] = c

for i in range(1, n+1):
    arr[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] != 1e9 and arr[i][j] != 0:
            visited[i][j] = [i, j]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                visited[i][j] = visited[i][k][:-1] + visited[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == 1e9:
            arr[i][j] = 0

for i in range(1, n+1):
    print(*arr[i][1:])

for i in range(1, n+1):
    for v in visited[i][1:]:
        print(len(v), *v)