from collections import deque

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque([])
queue.append([1, 0])
visited = [False] * (n+1)
visited[1] = True

while queue:
    x, y = queue.popleft()
    if y != 2:
        for nx in arr[x]:
            if not visited[nx]:
                queue.append([nx, y+1])
                visited[nx] = True

answer = 0
for i in range(2, n+1):
    if visited[i]:
        answer += 1

print(answer)