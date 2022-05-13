import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x, y):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
    
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)