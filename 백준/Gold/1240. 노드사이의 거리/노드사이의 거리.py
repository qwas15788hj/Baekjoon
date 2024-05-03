import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(m):
    s, e = map(int, input().split())
    queue = []
    visited = [1e9] * (n+1)
    heapq.heappush(queue, (s, 0))
    visited[s] = 0

    while queue:
        now, now_dist = heapq.heappop(queue)
        if visited[now] < now_dist:
            continue

        for nxt in arr[now]:
            nxt_dist = now_dist + nxt[1]
            if visited[nxt[0]] > nxt_dist:
                visited[nxt[0]] = nxt_dist
                queue.append((nxt[0], nxt_dist))

    print(visited[e])