from heapq import heappush, heappop

def dijkstra(start):
    queue = []
    heappush(queue, [0, start])
    visited = [1e9] * (n+1)
    visited[start] = 0

    while queue:
        c, x = heappop(queue)
        if visited[x] < c:
            continue
        for nx, nc in arr[x]:
            if visited[nx] > c + nc:
                visited[nx] = c + nc
                heappush(queue, [c + nc, nx])

    return visited


tc = int(input())
for _ in range(tc):
    # 입력 및 그래프 그리기
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a].append([b, d])
        arr[b].append([a, d])
    target = []
    for _ in range(t):
        target.append(int(input()))

    ds = dijkstra(s)
    dg = dijkstra(g)
    dh = dijkstra(h)

    answer = []
    for tg in target:
        # s -> tg 최소시간
        check = ds[tg]
        # s -> g -> h -> tg
        result1 = ds[g] + dg[h] + dh[tg]
        # s -> h -> g -> tg
        result2 = ds[h] + dh[g] + dg[tg]

        if check == min(result1, result2):
            answer.append(tg)

    answer.sort()
    print(*answer)