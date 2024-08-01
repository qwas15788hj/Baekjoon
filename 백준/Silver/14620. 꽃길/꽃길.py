from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a = [i for i in range(n*n)]
comb = list(combinations(a, 3))

# 범위 안에 있는지 체크
def check(x1, y1, x2, y2, x3, y3):
    flag = True
    if x1 == 0 or x1 == n-1:
        flag = False
    if y1 == 0 or y1 == n-1:
        flag = False
    if x2 == 0 or x2 == n-1:
        flag = False
    if y2 == 0 or y2 == n-1:
        flag = False
    if x3 == 0 or x3 == n-1:
        flag = False
    if y3 == 0 or y3 == n-1:
        flag = False
    return flag

answer = 1e9
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
for f1, f2, f3 in comb:
    x1, y1 = f1//n, f1%n
    x2, y2 = f2//n, f2%n
    x3, y3 = f3//n, f3%n
    # 범위 안 체크
    if not check(x1, y1, x2, y2, x3, y3):
        continue

    # 중복 체크
    num = [[0]*n for _ in range(n)]
    for i in range(5):
        num[x1+dx[i]][y1+dy[i]] += 1
        num[x2+dx[i]][y2+dy[i]] += 1
        num[x3+dx[i]][y3+dy[i]] += 1

    num_check = True
    for i in range(n):
        for j in range(n):
            if num[i][j] > 1:
                num_check = False
                break
        if num_check == False:
            break

    total = 0
    if num_check:
        for i in range(5):
            total += arr[x1+dx[i]][y1+dy[i]]
            total += arr[x2+dx[i]][y2+dy[i]]
            total += arr[x3+dx[i]][y3+dy[i]]
        answer = min(answer, total)

print(answer)