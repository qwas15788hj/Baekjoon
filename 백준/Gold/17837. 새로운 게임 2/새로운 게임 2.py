n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
piece = []
loca = [[[] for _ in range(n)] for _ in range(n)] # 위치 배열
for i in range(k):
    a, b, d = map(int, input().split())
    piece.append([a-1, b-1, d-1])
    loca[a-1][b-1] = [i]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0
flag = False
# 1000번 이상 진행
for _ in range(1001):
    for i in range(len(piece)):
        x, y, d = piece[i]
        nx = x + dx[d]
        ny = y + dy[d]

        # 파란색이거나 밖이면
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 2:
            # 방향 조절
            if d%2 == 0:
                d += 1
            else:
                d -= 1
            piece[i][2] = d
            nx = x + dx[d]
            ny = y + dy[d]
            # 반대도 파랑색이거나 밖인 경우 중단
            if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 2:
                continue

        # 움직이는 말 체크
        idx = loca[x][y].index(i)
        move = loca[x][y][idx:]
        loca[x][y] = loca[x][y][:idx] # 현재 칸 제거

        if arr[nx][ny] == 0: # 흰색
            loca[nx][ny] += move
        elif arr[nx][ny] == 1: # 빨간색
            loca[nx][ny] += move[::-1]

        # 이동한 말 모두 위치 변경
        for m in move:
            piece[m][0], piece[m][1] = nx, ny

        if len(loca[nx][ny]) >= 4:
            flag = True
            break

    answer += 1

    if flag:
        break

if flag:
    print(answer)
else:
    print(-1)