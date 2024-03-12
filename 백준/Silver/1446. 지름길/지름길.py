n, d = map(int, input().split())
arr = [i for i in range(d+1)]
short = []
for _ in range(n):
    s, e, d = map(int, input().split())
    short.append([s, e, d])

for i in range(1, len(arr)):
    arr[i] = min(arr[i], arr[i-1]+1)
    for s, e, dis in short:
        if i == e:
            arr[i] = min(arr[i], arr[s] + dis)

print(arr[-1])