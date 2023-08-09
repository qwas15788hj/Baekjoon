from collections import deque

def bfs(i, j, maps, visited): # bfs 함수 생성
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    
    n = len(maps) # 세로 길이
    m = len(maps[0]) # 가로 길이
    
    queue = deque() # 큐 생성
    queue.append([i, j]) # 큐에 위치인 i, j 값 저장
    visited[i][j] = True # i, j 위치 방문 처리
    count = 0 # 머물 수 있는 총 요일 수
    
    while queue: # 큐가 빌때까지 무한 루프 생성
        x, y = queue.popleft() # 큐에서 현재 위치 빼기
        count += int(maps[x][y]) # 현재 위치 총 요일에 더하기
        for i in range(4): # 다음 방향을 위해 네 방향 탐색
            nx = x + dx[i] # 다음 방향
            ny = y + dy[i]
            # 다음 방향이 범위 안에 있고, X가 아니며, 방문 안했다면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and not visited[nx][ny]:
                queue.append([nx, ny]) # 큐에 넣고
                visited[nx][ny] = True # 방문 처리
    
    return count
        

def solution(maps):
    answer = []
    
    n = len(maps) # 세로 길이
    m = len(maps[0]) # 가로 길이
    visited = [[False] * m for _ in range(n)] # 방문 처리 배열 생성
    
    # maps을 돌면서
    for i in range(n):
        for j in range(m):
            # 해당 위치가 X가 아니고 방문하지 않았다면
            if maps[i][j] != "X" and not visited[i][j]:
                # bfs함수 돌면서 return된 count 값 answer에 저장
                answer.append(bfs(i, j, maps, visited))
    
    # answer에 요소가 없다면 -1 저장
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort() # 오름차순 정렬
    
    return answer