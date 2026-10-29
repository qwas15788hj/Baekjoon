from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                count = 0
                queue = deque([[i, j]])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    count += int(maps[x][y])
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            queue.append([nx, ny])
                            visited[nx][ny] = True
                answer.append(count)
    
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    return answer