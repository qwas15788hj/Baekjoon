from collections import deque

n = int(input()) # 맵 크기 입력
arr = [] # 맵
for _ in range(n): # 맵 입력
    arr.append(list(map(int, input().split())))

shark_size = 2 # 초기 상어 크기
shark_eat = 0 # 상어가 먹은 물고기 개수
shark_x = 0 # 상어 위치 세로 값
shark_y = 0 # 상어 위치 가로 값
answer = 0 # 정답 개수

for i in range(n): # 초기 상어 위치 체크
    for j in range(n):
        if arr[i][j] == 9:
            shark_x = i
            shark_y = j
            break

def can_eat(arr): # 상어가 먹을 수 있는 물고기가 있는지 판단하는 함수
    global shark_size, n
    flag = False # 가능 한지 체크
    for i in range(n): # 맵 돌면서
        for j in range(n):
            if arr[i][j] < shark_size and arr[i][j] != 0: # 상어보다 작고, 빈칸이 아니면 => 먹을 물고기 있다
                flag = True # 가능함
                break
        if flag:
            break
    return flag # 판단 여부 리턴

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(arr): # 상어가 먹을 물고기 찾는 함수
    global shark_x, shark_y, n # 상어 위치
    queue = deque([]) # 큐 생성
    queue.append([shark_x, shark_y]) # 큐에 상어 위치 저장
    visited = [[0]*n for _ in range(n)] # 방문 체크 배열
    visited[shark_x][shark_y] = 1 # 첫 상어 위치 체크
    fish = [] # 먹을 수 있는 물고기 배열
    while queue: # 큐 돌면서
        size = len(queue) # 큐 사이즈 체크
        for i in range(size): # 큐 사이즈 만큼 돌면서
            x, y = queue.popleft() # 큐에서 빼기
            for j in range(4): # 4방향 보면서
                nx = x+dx[j]
                ny = y+dy[j]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and arr[nx][ny] <= shark_size: # 범위에 있고, 방문안하고, 상어크기보다 작거나 같으면 갈수있다
                    queue.append([nx, ny]) # 큐에 넣어주고
                    visited[nx][ny] = visited[x][y] + 1 # 이전방문+1 시간
                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0: # 상어크기보다 작고, 0이 아니면 먹을 수 있는 물고기!
                        fish.append([visited[nx][ny], nx, ny]) # 먹을 수 있는 물고기 배열에 방문시간, 세로값, 가로값 저장

    return fish # 물고기 배열 리턴

while True: # 계속 반복하면서
    if not can_eat(arr): # 먹을게 없으면 끝
        break
    else: # 먹을 물고기 존재한다면
        fish = bfs(arr) # 먹을 수 있는 물고기배열 받고
        fish.sort(key=lambda x:(x[0], x[1], x[2])) # 가까운 순, 가장 위, 가장 왼쪽 순으로 정렬
        if len(fish) == 0: # 먹을 물고기가 있음에도 갈 수 없는 경우!!! (반례)
            break
        # 2
        # 3 9
        # 1 3 => 1을 먹을 수 있음에도 3때매 못감
        eat_fish = fish[0] # 이번에 먹을 물고기
        arr[shark_x][shark_y] = 0 # 상어위치 0으로 초기화
        shark_x = eat_fish[1]
        shark_y = eat_fish[2] # 먹을 물고기로 상어 이동
        arr[shark_x][shark_y] = 9 # 이동한 상어 위치 9로 갱신!
        shark_eat += 1 # 상어 먹은 갯수 + 1
        answer += eat_fish[0]-1 # 상어가 먹은 물고기 가는데 걸리는 시간 더해주기(시작점이 1이였으니 -1)
        if shark_eat == shark_size: # 상어 먹은 개수가 사이즈랑 같다면
            shark_size += 1 # 사이즈 업
            shark_eat = 0 # 먹은 수 초기화

print(answer)