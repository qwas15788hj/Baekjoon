from itertools import product
from collections import deque

def solution(n, infection, edges, k):
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    max_num = 0
    for a, b, c in edges:
        arr[a].append([b, c])
        arr[b].append([a, c])
        max_num = max(max_num, c)
    
    prod = list(product(range(1, max_num+1), repeat=k))
    # 모든 경우의 수
    for pro in prod:
        queue = deque([])
        visited = [False] * (n+1)
        visited[infection] = True
        # 현재 큰 경우의 수 중 하나의 파이프 열기
        for pipe in pro:
            # 이전까지의 바이러스가 퍼진 곳 모두 큐에 저장
            for i in range(n+1):
                if visited[i]:
                    queue.append(i)
            # 바이러스 퍼지는 로직 실행
            while queue:
                x = queue.popleft()
                for nx, p in arr[x]:
                    # 다음 위치가 열리는 파이프이며, 방문하지 않았을 경우 추가
                    if pipe == p and not visited[nx]:
                        queue.append(nx)
                        visited[nx] = True
        
        answer = max(answer, visited.count(True))
                
    return answer