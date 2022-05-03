from sys import*
setrecursionlimit(10**6)

def dfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if maps[x][y] == 1:
        maps[x][y] = 0
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False
    
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
                dfs(i, j)
                count += 1
    print(count)