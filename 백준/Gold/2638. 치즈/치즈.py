from collections import deque
n, m = map(int, input().split()) # n, m 입력
cheeze = [] # 치즈 배열 생성
for _ in range(n): # 배열 입력
    cheeze.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
answer = 0 # 총 걸린 시간
while True: # 무한 루프 시작
    total = 0 # 치즈 배열의 총합
    for i in range(n): # 총합 구하기
        total += sum(cheeze[i])
    if total == 0: # 총합이 0이면 다 녹았음으로 무한 루프 종료
        break

    queue = deque() # 큐 생성
    check = [[False] * m for _ in range(n)] # 외부 공기인지 내부 공기인지 체크
    queue.append([0, 0]) # 큐에 맨 처음 시작점 (무조건 외부 공기) 저장
    check[0][0] = True # 시작점 체크
    # 외부 공기만 큐에 저장해서 치즈가 몇 개의 외부공기와 만나는지 확인
    while queue: # 큐가 빌 때까지
        x, y = queue.popleft() # 현재 위치 꺼내기
        for i in range(4): # 네 방향 탐색
            nx, ny = x + dx[i],  y + dy[i] # 다음 위치
            # 다음 위치가 범위 안에 있고, 아직 방문 안했다면
            if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
                if cheeze[nx][ny]: # 만약 해당 위치가 치즈면
                    cheeze[nx][ny] += 1 # 치즈 + 1 (치즈가 외부 공기와 만남, 큐에 저장 X)
                else: # 해당 위치가 치즈가 아니면 (외부 공기)
                    check[nx][ny] = True # 해당 위치 체크
                    queue.append([nx, ny]) # 큐에 저장

    # 치즈의 모든 부분을 돌면서
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] >= 3: # 현재 위치의 치즈 값이 3이상이면 (기존 1 + 외부 공기 2 이상)
                cheeze[i][j] = 0 # 현재 위치의 치즈 녹이기
            elif 0 < cheeze[i][j] < 3: # 현재 위치의 치즈 값이 1이나 2면 (기존 1 or 기존 1 + 공기 1)
                cheeze[i][j] = 1 # 원래 그대로인 값인 1로 갱신

    answer += 1 # 1초 증가

print(answer)