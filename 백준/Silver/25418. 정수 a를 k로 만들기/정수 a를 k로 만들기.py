from collections import deque

a, k = map(int, input().split())

queue = deque([])
visited = [0] * 1000001
queue.append(a)
visited[a] = 1
while queue:
    x = queue.popleft()
    if x+1 <= k and visited[x+1] == 0:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)
    if x*2 <= k and visited[x*2] == 0:
        visited[x*2] = visited[x] + 1
        queue.append(x*2)

print(visited[k]-1)