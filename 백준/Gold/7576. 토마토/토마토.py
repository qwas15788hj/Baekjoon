from collections import deque
m, n = map(int, input().split())
graph = []
queue = deque([])
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                
bfs()
answer = 0
for i in graph:
  for j in i:
    if j == 0:
        print(-1)
        exit(0)
    elif j > answer:
        answer = j
print(answer-1)