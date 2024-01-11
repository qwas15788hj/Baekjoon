import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for a in arr:
    a.sort(reverse=True)

def bfs(t):
    global cnt
    queue = deque()
    queue.append(t)
    visited[t] = cnt

    while queue:
        x = queue.popleft()
        for nx in arr[x]:
            if not visited[nx]:
                queue.append(nx)
                cnt += 1
                visited[nx] = cnt

cnt = 1
bfs(r)
for i in range(1, len(visited)):
    print(visited[i])