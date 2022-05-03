from sys import*
setrecursionlimit(10**6)
m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        global count
        count += 1
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0
answer = []

for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(count)
            result += 1
            count = 0
            
answer.sort()
print(result)
for i in answer:
    print(i, end=" ")