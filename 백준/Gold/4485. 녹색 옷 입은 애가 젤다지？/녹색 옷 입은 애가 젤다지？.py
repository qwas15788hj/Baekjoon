from heapq import heappush, heappop

count = 0
while True:
    n = int(input())
    if n == 0:
        break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    queue = []
    heappush(queue, [arr[0][0], 0, 0])
    visited =[[1e9] * n for _ in range(n)]
    visited[0][0] = arr[0][0]
    while queue:
        c, x, y = heappop(queue)
        if x == n-1 and y == n-1:
            answer = c
            break

        if visited[x][y] < c:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > c + arr[nx][ny]:
                    visited[nx][ny] = c + arr[nx][ny]
                    heappush(queue, [c + arr[nx][ny], nx, ny])

    count += 1
    print(f"Problem {count}: {answer}")