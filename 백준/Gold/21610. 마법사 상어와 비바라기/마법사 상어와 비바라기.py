import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]

answer = 0
for _ in range(m):
    d, s = map(int, input().split())

    # 구름 이동
    for i in range(len(cloud)):
        x, y = cloud[i]
        x = ((x + (dx[d-1] * s)) + n) % n
        y = ((y + (dy[d-1] * s)) + n) % n
        cloud[i] = (x, y)

    # 비가 1씩 내림
    for x, y in cloud:
        arr[x][y] += 1

    # 대각선 체크
    for x, y in cloud:
        for i in range(1, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != 0:
                    arr[x][y] += 1

    # 구름 생성
    nxt_cloud = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in cloud:
                arr[i][j] -= 2
                nxt_cloud.append([i, j])

    cloud = nxt_cloud

for i in arr:
    answer += sum(i)

print(answer)