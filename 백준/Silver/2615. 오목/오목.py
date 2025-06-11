import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

dx = [-1, -1, 0, 1]
dy = [0, 1, 1, 1]

def check(x, y):
    for k in range(4):
        min_x, min_y = x, y
        count = 1
        for i in range(-1, 2, 2):
            nx, ny = x, y
            while True:
                nx += i*dx[k]
                ny += i*dy[k]
                if 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == arr[x][y]:
                    count += 1
                    if min_y > ny or (min_y == ny and min_x > nx):
                        min_x, min_y = nx, ny
                else:
                    break

        if count == 5:
            return min_x, min_y
    else:
        return -1, -1

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            a, b = check(i, j)
            if a != -1 and b != -1:
                print(arr[i][j])
                print(a+1, b+1)
                exit()
else:
    print(0)