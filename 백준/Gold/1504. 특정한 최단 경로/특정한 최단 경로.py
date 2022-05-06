import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 정점, 거리
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF]*(n+1)
    heap = []
    heapq.heappush(heap, (start, 0))
    distance[start] = 0
    while heap:
        now, dist = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (i[0], cost))

    return distance


v1, v2 = map(int, input().split())

one_dis = dijkstra(1)
v1_dis = dijkstra(v1)
v2_dis = dijkstra(v2)

answer = min(one_dis[v1] + v1_dis[v2] + v2_dis[n], one_dis[v2] + v2_dis[v1] + v1_dis[n])
if answer >= INF:
    print(-1)
else:
    print(answer)