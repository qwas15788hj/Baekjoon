n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    arr.sort()
    arr[0], arr[1] = arr[0]+arr[1], arr[0]+arr[1]

print(sum(arr))