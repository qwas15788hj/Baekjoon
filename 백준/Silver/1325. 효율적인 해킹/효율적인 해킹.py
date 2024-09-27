import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

answer = [0] * (n+1)
for i in range(1, n+1):
    queue = deque([])
    visited = [False] * (n+1)
    queue.append(i)
    visited[i] = True
    while queue:
        x = queue.popleft()
        for nx in arr[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True

    answer[i] = visited.count(True)

max_count = max(answer)
for i in range(len(answer)):
    if answer[i] == max_count:
        print(i, end=" ")