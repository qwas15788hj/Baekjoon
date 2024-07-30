from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

queue = deque()
queue.append(a)
visited = [0] * (n+1)
visited[a] = 1
while queue:
    x = queue.popleft()
    for i in range(len(arr[x])):
        if not visited[arr[x][i]]:
            visited[arr[x][i]] = visited[x] + 1
            queue.append(arr[x][i])

print(visited[b]-1)