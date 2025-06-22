import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())

# 그래프 입력 (양방향)
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

# 질의마다 BFS 수행
for _ in range(q):
    k, v = map(int, input().split())
    queue = deque([])
    queue.append(v)
    visited = [1e9] * (n+1)
    while queue:
        x = queue.popleft()
        for nx, cost in arr[x]:
            if nx != v and visited[nx] == 1e9:
                queue.append(nx)
                # 경로 상 최소 USADO 갱신
                visited[nx] = min(visited[nx], visited[x])
                visited[nx] = min(visited[nx], cost)

    # 조건 만족 노드 개수 세기
    answer = 0
    for i in range(1, n+1):
        if visited[i] >= k:
            answer += 1

    print(answer-1)