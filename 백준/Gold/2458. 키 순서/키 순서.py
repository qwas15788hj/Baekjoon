import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
up, down = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    up[a].append(b)
    down[b].append(a)

def check(x, arr):
    queue = deque([])
    visited = [False] * (n+1)
    queue.append(x)
    visited[x] = True
    while queue:
        nx = queue.popleft()
        for mx in arr[nx]:
            if not visited[mx]:
                queue.append(mx)
                visited[mx] = True

    return visited

answer = 0
for i in range(1, n+1):
    s = set()
    v = check(i, up)
    for j in range(1, len(v)):
        if v[j]:
            s.add(j)
    v = check(i, down)
    for j in range(1, len(v)):
        if v[j]:
            s.add(j)

    if len(s) == n:
        answer += 1

print(answer)