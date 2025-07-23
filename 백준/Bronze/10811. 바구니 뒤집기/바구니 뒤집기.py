n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1

    arr = arr[:a] + arr[a:b][::-1] + arr[b:]

print(*arr)