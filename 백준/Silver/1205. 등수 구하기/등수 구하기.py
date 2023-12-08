n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    high, same = 0, 0
    for a in arr:
        if a > score:
            high += 1
        elif a == score:
            same += 1

    if high >= p:
        print(-1)
    else:
        if high + same >= p:
            print(-1)
        else:
            print(high + 1)