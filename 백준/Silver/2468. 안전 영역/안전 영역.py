from sys import*
setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False

n = int(input())
graph = []
min_high = 101
max_high = 0
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    a = list(map(int, input().split()))
    min_high = min(min_high, min(a))
    max_high = max(min_high, max(a))
    graph.append(a)

for high in range(max_high+1):
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= high:
                visited[i][j] = 1

    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                count += 1
    answer = max(answer, count)
    
print(answer)