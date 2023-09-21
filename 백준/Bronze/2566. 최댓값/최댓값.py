arr = [list(map(int, input().split())) for _ in range(9)] # 숫자 입력

m, x, y = 0, 0, 0 # 최대값, 세로, 가로
for i in range(9):
    for j in range(9):
        if arr[i][j] >= m:
            m = arr[i][j]
            x, y = i + 1, j + 1

print(m)
print(x, y)