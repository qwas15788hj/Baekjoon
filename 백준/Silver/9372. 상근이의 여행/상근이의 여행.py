import sys
input = sys.stdin.readline

# dfs 함수 생성 (현재 위치 지점, 카운트)
def dfs(now, cnt):
    visited[now] = True # 현재 지점 방문 체크
    for node in arr[now]: # 현재 지점 -> 다음 지점
        if not visited[node]: # 다음 지점을 방문 안했다면
            cnt = dfs(node, cnt + 1) # dfs 호출 (다음 지점, 카운트 1 증가) 한 것을 cnt 변수로
    return cnt # 재귀 종료시 cnt return

t = int(input()) # t 입력
for _ in range(t): # 테스트 케이스 반복
    n, m = map(int, input().split()) # n, m 입력
    arr = [[] for _ in range(n+1)] # 비행기 경로 배열 생성
    # 비행기 경로 입력 (양뱡향)
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b) # a -> b
        arr[b].append(a) # b -> a
    
    visited = [False] * (n+1) # 방문 처리
    visited[1] = True # 1번 여행지 방문
    print(dfs(1, 0)) # 1번 여행지 시작으로 dfs 탐색