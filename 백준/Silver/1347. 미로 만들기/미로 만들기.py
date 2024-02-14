n = int(input())
command = input()

arr = [["#"] * 101 for _ in range(101)]
x, y, dire = 50, 50, 2
arr[x][y] = "."
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

min_x, max_x, min_y, max_y = 50, 50, 50, 50

for com in command:
    if com == "F":
        x += dx[dire]
        y += dy[dire]
    elif com == "R":
        if dire == 3:
            dire = 0
        else:
            dire += 1
    elif com == "L":
        if dire == 0:
            dire = 3
        else:
            dire -= 1

    arr[x][y] = "."
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

for i in range(min_x, max_x+1):
    print("".join(arr[i][min_y:max_y+1]))