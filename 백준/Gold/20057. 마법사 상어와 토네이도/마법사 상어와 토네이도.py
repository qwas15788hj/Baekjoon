n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dire = []
visited = [[False] * n for _ in range(n)]
x, y = 0, -1
# 토네이도 순서 체크
while True:
    if x == n//2 and y == n//2:
        break
    for i in range(4):
        while True:
            x += dx[i]
            y += dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                x -= dx[i]
                y -= dy[i]
                break
            if visited[x][y]:
                x -= dx[i]
                y -= dy[i]
                break

            visited[x][y] = True
            dire.append([x, y, i])

# 방향 재설정
dire.reverse()
for i in range(len(dire)-1, 0, -1):
    dire[i][2] = (dire[i-1][2] + 2) % 4

answer = 0
# 좌풍
def left(x, y):
    global answer
    sand = arr[x][y]
    sand1 = (sand * 1)//100
    sand2 = (sand * 2)//100
    sand5 = (sand * 5)//100
    sand7 = (sand * 7)//100
    sand10 = (sand * 10)//100
    sand_a = sand - (sand1*2 + sand2*2 + sand5 + sand7*2 + sand10*2)

    # 1%
    if 0 <= x-1 and y+1 < n:
        arr[x-1][y+1] += sand1
    else:
        answer += sand1
    if x+1 < n and y+1 < n:
        arr[x+1][y+1] += sand1
    else:
        answer += sand1

    # 2%
    if 0 <= x-2:
        arr[x-2][y] += sand2
    else:
        answer += sand2
    if x+2 < n:
        arr[x+2][y] += sand2
    else:
        answer += sand2

    # 5%
    if 0 <= y-2:
        arr[x][y-2] += sand5
    else:
        answer += sand5

    # 7%
    if 0 <= x-1:
        arr[x-1][y] += sand7
    else:
        answer += sand7
    if x+1 < n:
        arr[x+1][y] += sand7
    else:
        answer += sand7

    # 10%
    if 0 <= x-1 and 0 <= y-1:
        arr[x-1][y-1] += sand10
    else:
        answer += sand10
    if x+1 < n and 0 <= y-1:
        arr[x+1][y-1] += sand10
    else:
        answer += sand10

    if 0 <= y-1:
        arr[x][y-1] += sand_a
    else:
        answer += sand_a

    arr[x][y] = 0

# 우풍
def right(x, y):
    global answer
    sand = arr[x][y]
    sand1 = (sand * 1) // 100
    sand2 = (sand * 2) // 100
    sand5 = (sand * 5) // 100
    sand7 = (sand * 7) // 100
    sand10 = (sand * 10) // 100
    sand_a = sand - (sand1*2 + sand2*2 + sand5 + sand7*2 + sand10*2)

    # 1%
    if 0 <= x-1 and 0 <= y-1:
        arr[x-1][y-1] += sand1
    else:
        answer += sand1
    if x+1 < n and 0 <= y-1:
        arr[x+1][y-1] += sand1
    else:
        answer += sand1

    # 2%
    if 0 <= x-2:
        arr[x-2][y] += sand2
    else:
        answer += sand2
    if x+2 < n:
        arr[x+2][y] += sand2
    else:
        answer += sand2

    # 5%
    if y+2 < n:
        arr[x][y+2] += sand5
    else:
        answer += sand5

    # 7%
    if 0 <= x-1:
        arr[x-1][y] += sand7
    else:
        answer += sand7
    if x+1 < n:
        arr[x+1][y] += sand7
    else:
        answer += sand7

    # 10%
    if 0 <= x-1 and y+1 < n:
        arr[x-1][y+1] += sand10
    else:
        answer += sand10
    if x+1 < n and y+1 < n:
        arr[x+1][y+1] += sand10
    else:
        answer += sand10

    if y+1 < n:
        arr[x][y+1] += sand_a
    else:
        answer += sand_a

    arr[x][y] = 0

# 상풍
def up(x, y):
    global answer
    sand = arr[x][y]
    sand1 = (sand * 1) // 100
    sand2 = (sand * 2) // 100
    sand5 = (sand * 5) // 100
    sand7 = (sand * 7) // 100
    sand10 = (sand * 10) // 100
    sand_a = sand - (sand1*2 + sand2*2 + sand5 + sand7*2 + sand10*2)

    # 1%
    if x+1 < n and 0 <= y-1:
        arr[x+1][y-1] += sand1
    else:
        answer += sand1
    if x+1 < n and y+1 < n:
        arr[x+1][y+1] += sand1
    else:
        answer += sand1

    # 2%
    if 0 <= y-2:
        arr[x][y-2] += sand2
    else:
        answer += sand2
    if y+2 < n:
        arr[x][y+2] += sand2
    else:
        answer += sand2

    # 5%
    if 0 <= x-2:
        arr[x-2][y] += sand5
    else:
        answer += sand5

    # 7%
    if 0 <= y-1:
        arr[x][y-1] += sand7
    else:
        answer += sand7
    if y+1 < n:
        arr[x][y+1] += sand7
    else:
        answer += sand7

    # 10%
    if 0 <= x-1 and 0 <= y-1:
        arr[x-1][y-1] += sand10
    else:
        answer += sand10
    if 0 <= x-1 and y+1 < n:
        arr[x-1][y+1] += sand10
    else:
        answer += sand10

    if 0 <= x-1:
        arr[x-1][y] += sand_a
    else:
        answer += sand_a

    arr[x][y] = 0

# 하풍
def down(x, y):
    global answer
    sand = arr[x][y]
    sand1 = (sand * 1) // 100
    sand2 = (sand * 2) // 100
    sand5 = (sand * 5) // 100
    sand7 = (sand * 7) // 100
    sand10 = (sand * 10) // 100
    sand_a = sand - (sand1*2 + sand2*2 + sand5 + sand7*2 + sand10*2)

    # 1%
    if 0 <= x-1 and 0 <= y-1:
        arr[x-1][y-1] += sand1
    else:
        answer += sand1
    if 0 <= x-1 and y+1 < n:
        arr[x-1][y+1] += sand1
    else:
        answer += sand1

    # 2%
    if 0 <= y-2:
        arr[x][y-2] += sand2
    else:
        answer += sand2
    if y+2 < n:
        arr[x][y+2] += sand2
    else:
        answer += sand2

    # 5%
    if x+2 < n:
        arr[x+2][y] += sand5
    else:
        answer += sand5

    # 7%
    if 0 <= y-1:
        arr[x][y-1] += sand7
    else:
        answer += sand7
    if y+1 < n:
        arr[x][y+1] += sand7
    else:
        answer += sand7

    # 10%
    if x+1 < n and 0 <= y-1:
        arr[x+1][y-1] += sand10
    else:
        answer += sand10
    if x+1 < n and y+1 < n:
        arr[x+1][y+1] += sand10
    else:
        answer += sand10

    if x+1 < n:
        arr[x+1][y] += sand_a
    else:
        answer += sand_a

    arr[x][y] = 0

for i in range(1, len(dire)):
    x, y, d = dire[i]
    if d == 0:
        right(x, y)
    elif d == 1:
        down(x, y)
    elif d == 2:
        left(x, y)
    elif d == 3:
        up(x, y)

print(answer)