from collections import deque

n, m = map(int, input().split()) # n, m 입력
trust = list(map(int, input().split())) # 진실을 아는 사람 리스트 (맨 앞은 명 수)
party = [] # 모든 파티 저장할 배열
for _ in range(m): # m 반복
    party.append(list(map(int, input().split()))) # 파티 저장 (리스트 마다 맨 앞은 명 수)

arr = [[0] * (n+1) for _ in range(n+1)] # 누구와 연결되어있는지
for i in range(len(party)): # 모든 파티를 돌면서
    for j in range(1, len(party[i])): # 현재 사람이
        idx1 = party[i][j] # 현재 파티의 현재 사람
        for z in range(1, len(party[i])): # 누구와 함께 하는지
            idx2 = party[i][z] # 현재 파티에서 함께하는 사람
            arr[idx1][idx2] = 1 # 체크
            arr[idx2][idx1] = 1 # 반대도 체크

queue = deque() # 큐 생성
know = [False] * (n+1) # 진실을 아는 사람 저장할 배열
for t in trust[1:]: # 진실 아는 사람 큐에 넣고, 체크
    queue.append(t)
    know[t] = True

while queue: # 큐가 빌 때까지
    x = queue.popleft() # 현재 사람
    for i in range(n+1): # n 까지 탐색
        if arr[x][i] == 1 and not know[i]: # 현재 사람과 함께 파티에 있고, 아직 진실을 모르는 사람이면
            queue.append(i) # 큐에 넣고
            know[i] = True # 진실 체크

answer = 0
for p in party: # 모든 파티 탐색하며
    for j in p[1:]: # 해당 파티에 참여한 인원을 탐색하며
        if know[j]: # 해당 인원이 사실을 알고 있다면 종료
            break
    else: # 그런 인원이 한 명도 존재하지 않는다면
        answer += 1 # answer 증가

print(answer)