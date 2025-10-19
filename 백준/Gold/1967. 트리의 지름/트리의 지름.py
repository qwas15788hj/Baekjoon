import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]
leaf = [True] * (n+1)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
    leaf[a] = False

answer = 0
for start in range(1, n+1):
    if leaf[start]:
        queue = deque()
        queue.append(start)
        visited = [0] * (n+1)
        visited[start] = 0
        while queue:
            x = queue.popleft()
            for nx, nc in arr[x]:
                if nx != start and visited[nx] == 0:
                    queue.append(nx)
                    visited[nx] = visited[x] + nc

        answer = max(answer, max(visited))

print(answer)