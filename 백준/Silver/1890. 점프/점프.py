n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and arr[i][j] != 0:
            x, y = i + arr[i][j], j + arr[i][j]
            if 0 <= x < n:
                dp[x][j] += dp[i][j]
            if 0 <= y < n:
                dp[i][y] += dp[i][j]

print(dp[-1][-1])