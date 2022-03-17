t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        print(1)
    else:
        d = [0]*(n+1)
        d[1], d[2] = 1, 1
        for i in range(3, n+1):
            d[i] = d[i-3] + d[i-2]
        print(d[n])