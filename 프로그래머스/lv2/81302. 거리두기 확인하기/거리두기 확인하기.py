from collections import deque

def solution(places):
    answer = []
    
    # 강의장 1개씩 확인
    for place in places:
        # 응시자가 있는 최초 P 지점 저장
        start = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    start.append([i, j])
        
        flag = True # 거리두기 확인
        
        # 모든 P 확인
        for s in start:
            queue = deque() # 큐 생성
            visited = [[False] * 5 for _ in range(5)] # 방문 처리
            dist = [[0] * 5 for _ in range(5)] # 거리 저장
            
            s_x, s_y = s[0], s[1] # 시작 지점
            queue.append([s_x, s_y]) # 최초 시작점 큐에 저장
            visited[s_x][s_y] = True # 시작점 방문 체크
            
            dx = [0, 0, -1, 1] # 상하좌우
            dy = [-1, 1, 0 ,0]
            
            while queue: # 큐 빌 때까지
                x, y = queue.popleft() # 현재 위치
                # 현재 위치에 사람이 있고, 거리가 2이하고, 현재 위치가 시작 지점이 아니면
                if place[x][y] == "P" and dist[x][y] <= 2 and (x != s_x or y != s_y):
                    flag = False # 거리두기 실패 및 종료
                    break
                    
                for i in range(4): # 네 방향 탐색
                    nx, ny = x + dx[i], y + dy[i] # 다음 방향
                    # 다음 방향이 범위 안에 있고, 방문 안했고, 벽이 아니면
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != "X":
                        queue.append([nx, ny]) # 큐에 다음 방향 넣고
                        visited[nx][ny] = True # 방문 체크
                        dist[nx][ny] = dist[x][y] + 1 # 다음 거리 = 현재 거리 + 1로 갱신
            
            # 모든 P 탐색 전 이미 거리두기 실패면 종료
            if flag == False:
                answer.append(0)
                break
                
        # 모든 탐색 이후 거리두기 성공이면
        if flag:
            answer.append(1)
        
    return answer