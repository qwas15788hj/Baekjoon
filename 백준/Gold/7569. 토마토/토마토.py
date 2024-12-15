from collections import deque

m, n, h = map(int, input().split()) # m, n, h 입력
arr = [[] for _ in range(h)] # 2차원 배열 생성
for i in range(h): # 2차원 배열에 높이에 맞게끔 배열 삽입하여 3차원 배열 생성
    for _ in range(n):
        arr[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1] # 6방향, 앞 뒤 왼 오 위 아래

def bfs(tomato): # 토마토 익히는 함수
    queue = deque([]) # 큐 생성
    for tmt in tomato: # 토마토 위치
        queue.append(tmt) # 큐에 넣어주기
    time = 0 # 시간 측정
    while queue: # 큐 돌면서
        size = len(queue) # 큐 크기
        for i in range(size): # 큐 크기만큼
            z, x, y = queue.popleft() # h, n, m 순으로 받아야함
            for j in range(6): # 6방향 돌면서
                nz = z+dz[j]
                nx = x+dx[j]
                ny = y+dy[j]
                if 0<=nz<h and 0<=nx<n and 0<=ny<m and arr[nz][nx][ny] == 0: # 범위에 있고, 안익은 토마토가 있으면 익혀주기
                    arr[nz][nx][ny] = 1 # 토마토 익혀주고
                    queue.append([nz, nx, ny]) # 큐에 위치 넣어주기
        time += 1 # 큐 다 돌았으면 시간 증가
    return time-1 # 마지막은 바로 끝나면 되지만 해당 함수에서는 시간을 증가하고 끝나기에 -1

def check(arr): # 토마토가 다 익었는지 판단하는 함수
    for i in range(h): # 높이
        for j in range(n): # 세로
            for k in range(m): # 가로
                if arr[i][j][k] == 0: # 해당 부분에 익지않은 토마토가 있다면
                    return False # false 리턴
    return True # 다 잘 돌았으면 true 리턴

tomato = [] # 맨처음 토마토 위치 담은 배열
for i in range(h): # 3차원
    for j in range(n): # 2차원
        for k in range(m): # 1차원
            if arr[i][j][k] == 1: # 상자 돌면서 토마토면 배열에 담기
                tomato.append([i, j, k]) # h, n, m 순으로 저장

time = bfs(tomato) # 토마토 익히는 함수
if check(arr): # 토마토 체크한 것이 성공이면
    print(time) # 익힌 시간 출력
else: # 익지 않은 토마토 있다면
    print(-1) # -1 출력