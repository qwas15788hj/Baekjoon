from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start_x, start_y = i, j
                break
    
    queue = deque()
    queue.append([start_x, start_y])

    visited = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    flag = False
    
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            if board[x][y] == "G":
                flag = True
                return answer
            for i in range(4):
                if not visited[x][y][i]:
                    nx, ny = x, y
                    while True:
                        nx += dx[i]
                        ny += dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                            break
                        visited[nx][ny][i] = True
                    
                    queue.append([nx - dx[i], ny - dy[i]])
                    visited[x][y][i] = True
        
        answer += 1
    
    if not flag:
        answer = -1
    
    return answer