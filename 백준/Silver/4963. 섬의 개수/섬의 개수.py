from collections import deque

def bfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        maps[x][y] = 0
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and nx < h and ny >= 0 and ny < w and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny))
    
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))
  
    count = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)