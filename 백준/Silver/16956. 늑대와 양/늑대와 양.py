import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sheep = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == "S":
            sheep.append([i, j])

flag = True
for x, y in sheep:
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == "W":
                flag = False
                break
            if arr[nx][ny] == ".":
                arr[nx][ny] = "D"

        if not flag:
            break
    if not flag:
        break

if flag:
    print(1)
    for i in arr:
        print("".join(i))
else:
    print(0)