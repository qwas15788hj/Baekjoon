import heapq, sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, i = map(int, input().split())
    arr[a].append([b, i])
    arr[b].append([a, i])

answer = 0
for start in range(1, n+1):
    queue = []
    heapq.heappush(queue, [start, 0])
    distance = [1e9] * (n+1)
    distance[start] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for nx, c in arr[now]:
            cost = dist + c
            if cost < distance[nx]:
                distance[nx] = cost
                heapq.heappush(queue, [nx, cost])

    count = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            count += item[i]

    answer = max(answer, count)

print(answer)