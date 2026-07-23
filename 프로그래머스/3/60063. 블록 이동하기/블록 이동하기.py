from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([[0, 0, 0, 1, 0]])
    visited = set()
    visited.add((0, 0, 0, 1))
    while queue:
        x1, y1, x2, y2, c = queue.popleft()
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1):
            return c
        
        # 네 방향 이동
        for k in range(4):
            nx1, ny1 = x1 + dx[k], y1 + dy[k]
            nx2, ny2 = x2 + dx[k], y2 + dy[k]
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                if (nx1, ny1, nx2, ny2) not in visited and (nx2, ny2, nx1, ny1) not in visited:
                    queue.append([nx1, ny1, nx2, ny2, c+1])
                    visited.add((nx1, ny1, nx2, ny2))
        
        # 왼쪽로봇(1), 오른쪽로봇(2) / 2가 1보다 오른쪽아래에 위치 -> 목적지와 가까워야함
        # 가로일 때
        if x1 == x2 and abs(y1-y2) == 1:
            # 왼쪽 로봇이 위로 이동
            nx1, ny1 = x1-1, y1+1
            cx1, cy1 = x1-1, y1
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= cx1 < n and 0 <= cy1 < n and board[nx1][ny1] == 0 and board[cx1][cy1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    queue.append([nx1, ny1, x2, y2, c+1])
                    visited.add((nx1, ny1, x2, y2))
            # 왼쪽 로봇이 아래로 이동
            nx1, ny1 = x1+1, y1+1
            cx1, cy1 = x1+1, y1
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= cx1 < n and 0 <= cy1 < n and board[nx1][ny1] == 0 and board[cx1][cy1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    # 1, 2 위치 변경
                    queue.append([x2, y2, nx1, ny1, c+1])
                    visited.add((x2, y2, nx1, ny1))
            # 오른쪽 로봇이 위로 이동
            nx2, ny2 = x2-1, y2-1
            cx2, cy2 = x2-1, y2
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= cx2 < n and 0 <= cy2 < n and board[nx2][ny2] == 0 and board[cx2][cy2] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    # 1, 2 위치 변경
                    queue.append([nx2, ny2, x1, y1, c+1])
                    visited.add((nx2, ny2, x1, y1))
            # 오른쪽 로봇이 아래로 이동
            nx2, ny2 = x2+1, y2-1
            cx2, cy2 = x2+1, y2
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= cx2 < n and 0 <= cy2 < n and board[nx2][ny2] == 0 and board[cx2][cy2] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    queue.append([x1, y1, nx2, ny2, c+1])
                    visited.add((x1, y1, nx2, ny2))            
            
        # 세로일 때    
        else:
            # 위쪽 로봇이 왼쪽으로 이동
            nx1, ny1 = x1+1, y1-1
            cx1, cy1 = x1, y1-1
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= cx1 < n and 0 <= cy1 < n and board[nx1][ny1] == 0 and board[cx1][cy1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    queue.append([nx1, ny1, x2, y2, c+1])
                    visited.add((nx1, ny1, x2, y2))
            # 위쪽 로봇이 오른쪽으로 이동
            nx1, ny1 = x1+1, y1+1
            cx1, cy1 = x1, y1+1
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= cx1 < n and 0 <= cy1 < n and board[nx1][ny1] == 0 and board[cx1][cy1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    # 1, 2 위치 변경
                    queue.append([x2, y2, nx1, ny1, c+1])
                    visited.add((x2, y2, nx1, ny1))
            # 아래쪽 로봇이 왼쪽으로 이동
            nx2, ny2 = x2-1, y2-1
            cx2, cy2 = x2, y2-1
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= cx2 < n and 0 <= cy2 < n and board[nx2][ny2] == 0 and board[cx2][cy2] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    # 1, 2 위치 변경
                    queue.append([nx2, ny2, x1, y1, c+1])
                    visited.add((nx2, ny2, x1, y1))
            # 아래쪽 로봇이 오른쪽으로 이동
            nx2, ny2 = x2-1, y2+1
            cx2, cy2 = x2, y2+1
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= cx2 < n and 0 <= cy2 < n and board[nx2][ny2] == 0 and board[cx2][cy2] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    queue.append([x1, y1, nx2, ny2, c+1])
                    visited.add((x1, y1, nx2, ny2))
    
    return answer