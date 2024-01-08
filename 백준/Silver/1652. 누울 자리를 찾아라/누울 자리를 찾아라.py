n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
width, length = 0, 0

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i][j] == ".":
            count += 1
        else:
            if count >= 2:
                width += 1
            count = 0

    if count >= 2:
        width += 1
        count = 0

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j][i] == ".":
            count += 1
        else:
            if count >= 2:
                length += 1
            count = 0

    if count >= 2:
        length += 1
        count = 0

print(width, length)