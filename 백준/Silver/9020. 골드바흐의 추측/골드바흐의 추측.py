t = int(input())
s = 10001
arr = [True] * (s+1)
for i in range(2, int(s**0.5) + 1):
    if arr[i]:
        for j in range(i*i, s+1, i):
            arr[j] = False

for _ in range(t):
    n = int(input())
    start, end = 0, 1e9
    for i in range(2, n//2 + 1):
        if arr[i] and arr[n-i]:
            if abs(i - (n-i)) < abs(start - end):
                start, end = i, (n-i)

    print(start, end)