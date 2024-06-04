from itertools import combinations

n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

def check(com):
    flag = True
    for i, j in com:
        arr[i][j] = "O"

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x, y in std:
        for k in range(4):
            nx, ny = x, y
            while True:
                nx += dx[k]
                ny += dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if arr[nx][ny] == "T":
                    flag = False
                    break
                if arr[nx][ny] == "O":
                    break

            if flag == False:
                break
        if flag == False:
            break

    for i, j in com:
        arr[i][j] = "X"

    return flag


std = []
wall = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "S":
            std.append([i, j])
        if arr[i][j] == "X":
            wall.append([i, j])

comb = list(combinations(wall, 3))
for com in comb:
    if check(com):
        print("YES")
        break
else:
    print("NO")