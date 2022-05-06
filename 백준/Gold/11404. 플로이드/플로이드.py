import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e9
distance = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distance[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < distance[a][b]:
        distance[a][b] = c

for r in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][r]+distance[r][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] >= INF:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()