from collections import deque

def solution(n, wires):
    answer = 1e9
    
    arr = [[0] * (101) for _ in range(101)] # 최대 100이하인 n 개의 정점 배열 생성
    for wire in wires: # 전력망 모두 탐색하며
        arr[wire[0]][wire[1]] = 1 # 연결 체크
        arr[wire[1]][wire[0]] = 1 # 반대 연결 체크
    
    for wire in wires: # 전력망 모두 탐색하며
        arr[wire[0]][wire[1]] = 0 # 현재 제거할 전력망 0으로 갱신
        arr[wire[1]][wire[0]] = 0
        
        queue = deque() # 큐 생성
        visited = [False] * (101) # 방문 체크
        queue.append(wire[0]) # 끊은 첫 번째 전력망 큐에 넣기
        visited[wire[0]] = True # 첫 번째 전력망 방문 체크
        cnt = 1 # 첫 번째 전력망과 연결된 전력망 개수 체크 (초기 1 자기 자신)
        
        while queue: # 큐가 빌 때까지
            now = queue.popleft() # 현재 체크할 전력망
            for i in range(101): # n까지 돌면서
                if arr[now][i] == 1 and not visited[i]: # 현재 전력망과 연결되어있고, 방문안했다면
                    queue.append(i) # 큐에 넣고
                    visited[i] = True # 방문 처리
                    cnt += 1 # 개수 증가
        
        # answer은 자신과 n개 중 cnt개수 뺀 것과 cnt 차이 중 작은 것으로 갱신
        answer = min(answer, abs((n - cnt) - cnt))
        arr[wire[0]][wire[1]] = 1 # 현재 체크한 전력망 다시 원상복구
        arr[wire[1]][wire[0]] = 1
    
    return answer