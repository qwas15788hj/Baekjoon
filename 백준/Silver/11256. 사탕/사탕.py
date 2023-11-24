t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append(a*b)
    arr.sort(reverse=True)

    idx = 0
    while j > 0:
        j -= arr[idx]
        idx += 1

    print(idx)