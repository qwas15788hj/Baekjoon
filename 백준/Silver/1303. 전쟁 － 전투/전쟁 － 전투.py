n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(str, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count_white = 0
count_blue = 0
answer_white = []
answer_blue = []

def dfs_white(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'W':
        global count_white
        count_white += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_white(nx, ny)
        return True
    return False

def dfs_blue(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 'B':
        global count_blue
        count_blue += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_blue(nx, ny)
        return True
    return False

for i in range(m):
    for j in range(n):
        if dfs_white(i, j) == True:
            answer_white.append(count_white)
            count_white = 0
        if dfs_blue(i, j) == True:
            answer_blue.append(count_blue)
            count_blue = 0
            
answer = []
score = 0
for w in answer_white:
    score += w**2
answer.append(score)

score = 0
for b in answer_blue:
    score += b**2
answer.append(score)

for i in answer:
    print(i, end=' ')