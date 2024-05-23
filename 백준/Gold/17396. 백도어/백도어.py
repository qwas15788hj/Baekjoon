import heapq, sys
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

queue = []
visited = [INF] * n
heapq.heappush(queue, [0, 0])
visited[0] = 0
while queue:
    now, cost = heapq.heappop(queue)
    if visited[now] < cost:
        continue
    for target, t_cost in graph[now]:
        if target == n-1 or arr[target] == 0:
            if visited[target] > cost + t_cost:
                visited[target] = cost + t_cost
                heapq.heappush(queue, [target, cost + t_cost])

if visited[n-1] == INF:
    print(-1)
else:
    print(visited[n-1])