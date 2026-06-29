from collections import deque

def solution(board):
    answer = 0
    
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([])
    visited = [[[1e9] * 4 for _ in range(n)] for _ in range(n)]
    if board[0][1] == 0:
        queue.append([0, 1, 1])
        visited[0][1][1] = 100
    if board[1][0] == 0:
        queue.append([1, 0, 2])
        visited[1][0][2] = 100
    
    while queue:
        x, y, d = queue.popleft()
        
        # 방향 그대로
        nx, ny = x + dx[d], y + dy[d]
        cost = visited[x][y][d] + 100
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny][d] > cost:
            queue.append([nx, ny, d])
            visited[nx][ny][d] = cost
        
        # 반시계 방향 회전
        nd = (d-1)%4
        nx, ny = x + dx[nd], y + dy[nd]
        cost = visited[x][y][d] + 600
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny][nd] > cost:
            queue.append([nx, ny, nd])
            visited[nx][ny][nd] = cost
        
        # 시계 방향 회전
        nd = (d+1)%4
        nx, ny = x + dx[nd], y + dy[nd]
        cost = visited[x][y][d] + 600
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny][nd] > cost:
            queue.append([nx, ny, nd])
            visited[nx][ny][nd] = cost
    
    return min(visited[-1][-1])