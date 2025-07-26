l, p = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(5):
    arr[i] -= l*p

print(*arr)