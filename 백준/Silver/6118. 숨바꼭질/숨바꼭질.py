from collections import deque

n, m = map(int ,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque([])
queue.append(1)
visited = [0] * (n+1)
visited[1] = 1
while queue:
    x = queue.popleft()
    for nx in arr[x]:
        if visited[nx] == 0:
            queue.append(nx)
            visited[nx] = visited[x] + 1

print(visited.index(max(visited)), max(visited)-1, visited.count(max(visited)))