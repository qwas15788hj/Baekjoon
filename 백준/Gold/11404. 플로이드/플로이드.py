n = int(input())
m = int(input())
visited = [[1e9] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    visited[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    visited[a][b] = min(visited[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

for i in range(1, n+1):
    a = []
    for j in range(1, n+1):
        if visited[i][j] == 1e9:
            visited[i][j] = 0
        a.append(visited[i][j])
    print(*a)