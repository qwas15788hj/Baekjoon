from collections import deque
from sys import *
setrecursionlimit(10**6)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x]+1
                queue.append(i)
                
bfs(a)
if visited[b] == 0:
    print(-1)
else:
    print(visited[b])