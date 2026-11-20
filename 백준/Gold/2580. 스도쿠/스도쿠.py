import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i, j])

# [i, j]에 v값이 들어가도 되는지 체크
def check(i, j, v):
    # 가로/세로 체크
    for k in range(9):
        if arr[i][k] == v:
            return False
        if arr[k][j] == v:
            return False

    sx = i//3*3
    sy = j//3*3
    for x in range(sx, sx+3):
        for y in range(sy, sy+3):
            if arr[x][y] == v:
                return False

    return True

def solve(k):
    if k == len(blank):
        for i in arr:
            print(*i)
        sys.exit(0)

    i, j = blank[k]
    for v in range(1, 10):
        if check(i, j, v):
            arr[i][j] = v
            solve(k+1)
            arr[i][j] = 0

solve(0)