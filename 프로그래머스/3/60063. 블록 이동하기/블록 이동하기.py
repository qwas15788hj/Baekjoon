from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([[0, 0, 0, 1, 0]])
    visited = set()
    visited.add((0, 0, 0, 1))
    visited.add((0, 0, 0, 1))
    while queue:
        x1, y1, x2, y2, c = queue.popleft()
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1):
            return c
        
        # 네 방향 이동
        for k in range(4):
            nx1, ny1 = x1 + dx[k], y1 + dy[k]
            nx2, ny2 = x2 + dx[k], y2 + dy[k]
            # 범위 안에 있고,
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                if (nx1, ny1, nx2, ny2) not in visited and (nx2, ny2, nx1, ny1) not in visited:
                    visited.add((nx1, ny1, nx2, ny2))
                    queue.append([nx1, ny1, nx2, ny2, c+1])
            
        # 방향 변경 (변경시 반드시 2가 1보다 우측이나 아래에 있어야 함)
        # 로봇이 가로 상태면
        if (x1 == x2) and (abs(y1-y2) == 1):
            # 왼쪽에 있는 1이 위로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            nx1, ny1 = x2-1, y2
            if 0 <= nx1 < n and 0 <= ny1 < n and board[nx1][ny1] == 0 and 0 <= x2-1 < n and 0 <= y2-1 < n and board[x2-1][y2-1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    visited.add((nx1, ny1, x2, y2))
                    queue.append([nx1, ny1, x2, y2, c+1])
            # 왼쪽에 있는 1이 아래로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            # 아래로 이동이기에 저장은 반대로
            nx1, ny1 = x2+1, y2
            if 0 <= nx1 < n and 0 <= ny1 < n and board[nx1][ny1] == 0 and 0 <= x2+1 < n and 0 <= y2-1 < n and board[x2+1][y2-1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    visited.add((x2, y2, nx1, ny1))
                    queue.append([x2, y2, nx1, ny1, c+1])
            # 오른쪽에 있는 2가 위로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            # 2가 위로 이동이기에 저장은 반대로
            nx2, ny2 = x1-1, y1
            if 0 <= nx2 < n and 0 <= ny2 < n and board[nx2][ny2] == 0 and 0 <= x1-1 < n and 0 <= y1+1 < n and board[x1-1][y1+1] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    visited.add((nx2, ny2, x1, y1))
                    queue.append([nx2, ny2, x1, y1, c+1])
            # 오른쪽에 있는 2가 아래로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            nx2, ny2 = x1+1, y1
            if 0 <= nx2 < n and 0 <= ny2 < n and board[nx2][ny2] == 0 and 0 <= x1+1 < n and 0 <= y1+1 < n and board[x1+1][y1+1] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    visited.add((x1, y1, nx2, ny2))
                    queue.append([x1, y1, nx2, ny2, c+1])    
                
                
        # 방향 변경 (변경시 반드시 2가 1보다 우측이나 아래에 있어야 함)
        # 로봇이 세로 상태면
        if (abs(x1-x2) == 1) and (y1 == y2):
            # 위쪽에 있는 1이 왼쪽로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            nx1, ny1 = x2, y2-1
            if 0 <= nx1 < n and 0 <= ny1 < n and board[nx1][ny1] == 0 and 0 <= x2-1 < n and 0 <= y2-1 < n and board[x2-1][y2-1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    visited.add((nx1, ny1, x2, y2))
                    queue.append([nx1, ny1, x2, y2, c+1])
            # 위쪽에 있는 1이 오른쪽로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            # 1이 오른쪽으로 이동이기에 반대로 저장
            nx1, ny1 = x2, y2+1
            if 0 <= nx1 < n and 0 <= ny1 < n and board[nx1][ny1] == 0 and 0 <= x2-1 < n and 0 <= y2+1 < n and board[x2-1][y2+1] == 0:
                if (nx1, ny1, x2, y2) not in visited and (x2, y2, nx1, ny1) not in visited:
                    visited.add((x2, y2, nx1, ny1))
                    queue.append([x2, y2, nx1, ny1, c+1])
            # 아래쪽에 있는 2가 왼쪽로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            # 2가 왼쪽으로 이동하기에 반대로 저장
            nx2, ny2 = x1, y1-1
            if 0 <= nx2 < n and 0 <= ny2 < n and board[nx2][ny2] == 0 and 0 <= x1+1 < n and 0 <= y1-1 < n and board[x1+1][y1-1] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    visited.add((nx2, ny2, x1, y1))
                    queue.append([nx2, ny2, x1, y1, c+1])
            # 아래쪽에 있는 2가 오른쪽으로 이동, 이동 위치와 이동 시 걸리는 곳 모두 범위 안에 있으며 0이여야함
            nx2, ny2 = x1, y1+1
            if 0 <= nx2 < n and 0 <= ny2 < n and board[nx2][ny2] == 0 and 0 <= x1+1 < n and 0 <= y1+1 < n and board[x1+1][y1+1] == 0:
                if (x1, y1, nx2, ny2) not in visited and (nx2, ny2, x1, y1) not in visited:
                    visited.add((x1, y1, nx2, ny2))
                    queue.append([x1, y1, nx2, ny2, c+1])    
    
    return answer