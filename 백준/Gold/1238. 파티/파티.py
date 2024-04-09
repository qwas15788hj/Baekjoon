import heapq, sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    arr[s].append((e, d))

answer = [0] * (n+1)

for j in range(1, n+1):
    queue = []
    visited = [1e9] * (n+1)
    heapq.heappush(queue, (j, 0))
    visited[j] = 0

    while queue:
        now, dist = heapq.heappop(queue)
        if visited[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))

    if j == x:
        for i in range(1, n+1):
            answer[i] += visited[i]
    else:
        answer[j] += visited[x]

print(max(answer))