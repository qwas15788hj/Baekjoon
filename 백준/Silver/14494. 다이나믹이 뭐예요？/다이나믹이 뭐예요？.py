n, m = map(int, input().split())

arr = [[1] * m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        arr[i][j] = (arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]) % 1000000007

print(arr[-1][-1] % 1000000007)