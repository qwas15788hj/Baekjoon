import heapq, sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
visited = [1e9] * (n+1)
start, end = map(int, input().split())

queue = []
heapq.heappush(queue, (start, 0))
visited[start] = 0
while queue:
    now, dist = heapq.heappop(queue)
    if visited[now] < dist:
        continue
    for i in arr[now]:
        cost = dist + i[1]
        if visited[i[0]] > cost:
            visited[i[0]] = cost
            heapq.heappush(queue, (i[0], cost))

print(visited[end])