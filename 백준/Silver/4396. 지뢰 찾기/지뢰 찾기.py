n = int(input())
arr = [list(input()) for _ in range(n)]
target = [list(input()) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
flag = False
for i in range(n):
    for j in range(n):
        if target[i][j] == "x":
            if arr[i][j] == "*":
                flag = True
            count = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n and arr[x][y] == "*":
                    count += 1

            target[i][j] = str(count)

if flag:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "*":
                target[i][j] = "*"

for i in range(n):
    print("".join(target[i]))