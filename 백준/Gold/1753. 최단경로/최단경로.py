import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
queue = []
heapq.heappush(queue, (0, K))
distance[K] = 0
while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))
            
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])