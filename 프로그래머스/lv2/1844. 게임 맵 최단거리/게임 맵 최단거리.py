from collections import deque

def solution(maps):
    
    queue = deque() # 큐 생성
    queue.append([0, 0]) # 큐에 시작점 생성
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    
    while queue: # 큐 반복
        x, y = queue.popleft() # 현재 위치
        for i in range(4): # 네 방향 돌면서
            nx = x + dx[i] # 다음 위치
            ny = y + dy[i]
            # 다음 위치가 범위 안에 있고, 갈 수 있다면
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 # 이전 값에 + 1 추가
                queue.append([nx, ny]) # 큐에 넣기
    
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]