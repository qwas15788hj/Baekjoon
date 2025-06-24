t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] * (n+1)
    d = 2
    while n != 1:
        if n%d == 0:
            n //= d
            arr[d] += 1
        else:
            d += 1

    for i in range(2, len(arr)):
        if arr[i] != 0:
            print(i, arr[i])