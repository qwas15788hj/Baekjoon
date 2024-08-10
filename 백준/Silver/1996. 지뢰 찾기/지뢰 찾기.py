n = int(input())
arr = [list(input()) for _ in range(n)]
map = [[0] * n for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(n):
    for j in range(n):
        if arr[i][j] != ".":
            num = int(arr[i][j])
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    map[x][y] += num

for i in range(n):
    for j in range(n):
        if map[i][j] >= 10:
            map[i][j] = "M"
        if arr[i][j] != ".":
            map[i][j] = "*"
        map[i][j] = str(map[i][j])

for i in range(n):
    print("".join(map[i]))