from collections import deque

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
queue = deque()
visited = [False] * n
queue.append(0)
visited[0] = True
count = 0
while queue:
    x = queue.popleft()
    if x == k:
        break
    if not visited[arr[x]]:
        queue.append(arr[x])
        visited[arr[x]] = True
    count += 1

if visited[k]:
    print(count)
else:
    print(-1)