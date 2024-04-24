n, m = map(int, input().split())

if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    answer = 1
    box = m
    for i in range(n):
        if box - arr[i] >= 0:
            box -= arr[i]
        else:
            box = m - arr[i]
            answer += 1

    print(answer)