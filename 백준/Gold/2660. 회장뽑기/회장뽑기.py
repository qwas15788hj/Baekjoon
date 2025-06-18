import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]

# 친구 사이 체크 (양방향 그래프)
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

# 친구 사이 거리 체크
result = [1e9] * (n+1)
for i in range(1, n+1):
    queue = deque()
    queue.append(i)
    visited = [0] * (n+1)
    visited[i] = 1
    while queue:
        x = queue.popleft()
        for nx in arr[x]:
            if visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1
    
    result[i] = max(visited[1:])-1

min_val = min(result) # 친구 거리 최솟값

# 출력
print(min_val, result.count(min_val))
for i in range(1, n+1):
    if result[i] == min_val:
        print(i, end=" ")