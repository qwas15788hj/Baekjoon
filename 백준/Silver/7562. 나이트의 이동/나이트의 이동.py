from collections import deque

t = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    queue = deque()
    visited = [[False] * l for _ in range(l)]
    queue.append([x, y])
    visited[x][y] = True
    time = 0
    while queue:
        size = len(queue)
        flag = False
        for _ in range(size):
            nx, ny = queue.popleft()
            if nx == target_x and ny == target_y:
                flag = True
                break

            for i in range(8):
                mx, my = nx + dx[i], ny + dy[i]
                if 0 <= mx < l and 0 <= my < l and not visited[mx][my]:
                    queue.append([mx, my])
                    visited[mx][my] = True

        if flag:
            break

        time += 1

    print(time)