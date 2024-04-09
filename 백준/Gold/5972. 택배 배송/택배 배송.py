import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

queue = []
heapq.heappush(queue, (1, 0))
visited[1] = 0
while queue:
    now, dist = heapq.heappop(queue)
    if visited[now] < dist:
        continue
    for i in arr[now]:
        cost = dist + i[1]
        if visited[i[0]] > cost:
            visited[i[0]] = cost
            heapq.heappush(queue, (i[0], cost))

print(visited[-1])