from collections import deque

n = int(input()) # n 입력
arr = list(map(int, input().split())) # 점프 입력
answer = 1e9 # 횟수

queue = deque() # 큐 생성
queue.append([0, 0]) # 큐에 현재 지점과 몇번 점프했는지 체크를 위해 초기 0, 0 저장
visited = [False] * 1101 # 최대 n 이 1000이고 점프가 100 임으로 1101 생성
visited[0] = True # 방문처리 최초 0 지점 체크

while queue:
    x, y = queue.popleft() # 현재 위치, 횟수 꺼내기
    if x >= n - 1: # 현재 위치가 가장 왼쪽에 도달햇으면
        answer = min(answer, y) # answer 갱신
    else: # 아직 도달 못햇으면
        # 해당 위치에서 점프할 수 있는 수 모두 체크
        for i in range(1, arr[x] + 1):
            nx = x + i # 다음 위치
            if not visited[nx]: # 다음 위치 방문 안했다면
                queue.append([nx, y + 1]) # 큐에 다음 위치, 횟수 + 1 저장
                visited[nx] = True # 다음 위치 방문 처리

if answer == 1e9:
    answer = -1

print(answer)