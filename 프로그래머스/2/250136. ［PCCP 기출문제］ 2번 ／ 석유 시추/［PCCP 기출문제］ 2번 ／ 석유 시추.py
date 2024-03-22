from collections import deque

def bfs(x, y, num, land, visited):
    n = len(land)
    m = len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = num
    count = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if 0 <= mx < n and 0 <= my < m and visited[mx][my] == 0 and land[mx][my] == 1:
                queue.append([mx, my])
                visited[mx][my] = num
                count += 1
    
    return count

def solution(land):
    answer = []
    dic = dict()
    
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                dic[num] = bfs(i, j, num, land, visited)
                num += 1
    
    for i in range(m):
        check = set()
        for j in range(n):
            check.add(visited[j][i])
        
        cnt = 0
        for s in list(check):
            if s in dic:
                cnt += dic[s]
                
        answer.append(cnt)
    
    return max(answer)