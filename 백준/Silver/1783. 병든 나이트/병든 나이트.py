n, m = map(int, input().split()) # 세로, 가로
count = 1
if n == 2:
    if m < 3:
        pass
    elif m < 5:
        count += 1
    elif m < 7:
        count += 2
    else:
        count += 3

elif n > 2:
    if m == 1:
        pass
    elif m == 2:
        count += 1
    elif m == 3:
        count += 2
    elif m < 7:
        count += 3
    else:
        count += 4+m-7

print(count)