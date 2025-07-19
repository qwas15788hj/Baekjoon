n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
for i in range(m):
    if arr[0][i] == "1":
        dp[0][i] = 1
for i in range(n):
    if arr[i][0] == "1":
        dp[i][0] = 1

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == "1":
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])
            dp[i][j] = min(dp[i][j-1], dp[i][j])
            dp[i][j] += 1

answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))

print(answer**2)