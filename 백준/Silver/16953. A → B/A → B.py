a, b = map(int, input().split())
count = 1

while True:
    if a == b:
        print(count)
        break
    elif (b%2 != 0 and b%10 != 1) or a > b:
        print(-1)
        break
    else:
        if b%10 == 1:
            b //= 10
            count += 1
        else:
            b //= 2
            count += 1