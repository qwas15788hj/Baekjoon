t = int(input())

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    now_x = 0
    now_y = 0
    dir = 0
    pos = [(now_x, now_y)]

    s = input()
    for i in s:
        if i == "F":
            now_x += dx[dir]
            now_y += dy[dir]
        elif i == "B":
            now_x -= dx[dir]
            now_y -= dy[dir]
        elif i == "L":
            if dir == 0:
                dir = 3
            else:
                dir -= 1
        elif i == "R":
            if dir == 3:
                dir = 0
            else:
                dir += 1
        pos.append((now_x, now_y))

    pos.sort(key=lambda x:x[0])
    x = pos[-1][0]-pos[0][0]
    pos.sort(key=lambda x:x[1])
    y = pos[-1][1]-pos[0][1]
    print(x*y)