r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bomb(map):
    now_map = [["O" for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if map[i][j] == "O":
                now_map[i][j] = "."
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < r and 0 <= y < c:
                        now_map[x][y] = "."

    return now_map

if n == 1:
    for i in arr:
        print("".join(i))
elif n%2 == 0:
    for i in range(r):
        print("O" * c)
elif n%4 == 3:
    answer = bomb(arr)
    for i in answer:
        print("".join(i))
elif n%4 == 1:
    answer = bomb(arr)
    answer = bomb(answer)
    for i in answer:
        print("".join(i))