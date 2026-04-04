from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 1
queue = deque([])
queue.append([x, y])
visited = [[False] * m for _ in range(n)]
visited[x][y] = True
loop_flag = True
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if arr[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        answer += 1

    # 청소되니 않은 빈 칸 체크
    flag = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if arr[nx][ny] == 0 and not visited[nx][ny]:
            flag = False

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if flag:
        nx, ny = x + dx[(d+2)%4], y + dy[(d+2)%4]
        # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            x, y = nx, ny
        # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            loop_flag = False
            break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 3-1. 반시계 방향으로 90도 회전한다.
        d = (d+3)%4
        # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny


    if not loop_flag:
        break

print(answer)