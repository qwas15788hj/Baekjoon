n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

answer = 0
flag = True
while flag:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if arr[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        answer += 1

    # 주변 4칸 체크
    check = True
    for k in range(4):
        nr = r + dx[k]
        nc = c + dy[k]
        # 청소되지 않은 곳 있으면 break
        if arr[nr][nc] == 0 and not visited[nr][nc]:
            check = False
            break
            
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if check:
        k = (d+2)%4
        # 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if arr[r+dx[k]][c+dy[k]] == 0:
            r += dx[k]
            c += dy[k]
        # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            flag = False
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 1. 반시계 방향으로 90도 회전한다.
        d = (d+4-1)%4
        # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        if arr[r+dx[d]][c+dy[d]] == 0 and not visited[r+dx[d]][c+dy[d]]:
            r += dx[d]
            c += dy[d]

print(answer)