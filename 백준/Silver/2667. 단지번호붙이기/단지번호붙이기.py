n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0
answer = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(count)
            result += 1
            count = 0
            
answer.sort()
print(result)
for i in answer:
    print(i)