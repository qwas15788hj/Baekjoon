c, r = map(int, input().split())
k = int(input())
arr = [[0] * c for _ in range(r)]
x, y = r-1, 0
target = 1
arr[x][y] = target

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if k > r * c:
    print(0)
else:
    while True:
        for i in range(4):
            while True:
                x += dx[i]
                y += dy[i]
                if target == k:
                    x -= dx[i]
                    y -= dy[i]
                    break
                if 0 <= x < r and 0 <= y < c and arr[x][y] == 0:
                    target += 1
                    arr[x][y] = target
                else:
                    x -= dx[i]
                    y -= dy[i]
                    break

            if target == k:
                break

        if target == k:
            break

    print(y+1, r-x)