from collections import deque

# bfs 길찾기 함수 생성
def bfs(maps, x, y, target):
    n = len(maps) # 맵 세로길이
    m = len(maps[0]) # 맵 가로길이
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    queue = deque() # 큐 생성
    queue.append([x, y]) # 현재 위치 x, y 큐에 저장
    visited = [[False] * m for _ in range(n)] # 방문 처리
    visited[x][y] = True # 현재 위치 방문 처리
    count = 0 # 시간
    
    while queue: # 큐가 빌 때까지
        size = len(queue) # 큐 사이즈만큼 반복
        for _ in range(size):
            # 현재 위치가 타겟이면 종료
            nx, ny = queue.popleft()
            if maps[nx][ny] == target:
                return count
            # 네 방향 탐색
            for i in range(4):
                mx = nx + dx[i]
                my = ny + dy[i]
                # 현재 위치가 범위 안에 있고, 방문 안했고, 벽이 아니면 방문
                if 0 <= mx < n and 0 <= my < m and not visited[mx][my] and maps[mx][my] != "X":
                    queue.append([mx, my])
                    visited[mx][my] = True
        
        count += 1 # 모든 큐 돌면 시간 증가
        
    return -1 # 못찾으면 -1 return
    
def solution(maps):
    
    s_x, s_y = 0, 0 # 시작 지점
    l_x, l_y = 0, 0 # 레버 지점
    # 시작, 레버 지점 찾기
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                s_x, s_y = i, j
            if maps[i][j] == "L":
                l_x, l_y = i, j
    
    # 레버 찾기 실패시 -1 return
    lever = bfs(maps, s_x, s_y, "L")
    if lever == -1:
        return -1
    
    # 끝 지점 찾기 실패시 -1 return
    end = bfs(maps, l_x, l_y, "E")
    if end == -1:
        return -1
    
    # 성공시 두개 합친 값 return
    return lever + end