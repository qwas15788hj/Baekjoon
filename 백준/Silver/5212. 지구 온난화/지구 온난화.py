r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
map = [["."] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(r):
    for j in range(c):
        if arr[i][j] == "X":
            count = 0
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < r and 0 <= y < c and arr[x][y] == "X":
                    count += 1
            if count >= 2:
                map[i][j] = "X"

s_x, e_x, s_y, e_y = 0, 0, 0, 0
for i in range(r):
    if "X" in map[i]:
        s_x = i
        break
for i in range(r-1, -1, -1):
    if "X" in map[i]:
        e_x = i
        break
for i in range(c):
    cnt = 0
    for j in range(r):
        if map[j][i] == "X":
            cnt += 1
    if cnt != 0:
        s_y = i
        break
for i in range(c-1, -1, -1):
    cnt = 0
    for j in range(r):
        if map[j][i] == "X":
            cnt += 1
    if cnt != 0:
        e_y = i
        break

for i in range(s_x, e_x+1):
    answer = ""
    for j in range(s_y, e_y+1):
        answer += map[i][j]
    print(answer)