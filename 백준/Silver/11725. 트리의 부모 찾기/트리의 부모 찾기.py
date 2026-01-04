from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque()
queue.append(1)
visited = [0] * (n+1)
visited[1] = 1
while queue:
    x = queue.popleft()
    for nx in arr[x]:
        if visited[nx] == 0:
            visited[nx] = x
            queue.append(nx)

for i in range(2, n+1):
    print(visited[i])