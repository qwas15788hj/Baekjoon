n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(m):
    a, b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

def bfs(v):
    visited[v] = True
    global count
    for i in graph[v]:
        if not visited[i]:
            bfs(i)
            count += 1

bfs(1)
print(count)