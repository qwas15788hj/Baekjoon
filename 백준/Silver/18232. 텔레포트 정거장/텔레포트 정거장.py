import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())
dic = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

queue = deque()
queue.append(s)
visited = [-1] * (n+1)
visited[s] = 0
while queue:
    x = queue.popleft()
    if 1 <= x-1 < n+1 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)
    if 1 <= x+1 < n+1 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)
    if x in dic:
        for nx in dic[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(visited[e])