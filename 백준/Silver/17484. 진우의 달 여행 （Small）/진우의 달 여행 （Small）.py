n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[1e9]*3 for _ in range(m)] for _ in range(n)]
for i in range(m):
    if i == 0:
        dp[1][i][1] = arr[0][i] + arr[1][i]
        dp[1][i][2] = arr[0][i+1] + arr[1][i]
    elif i == m-1:
        dp[1][i][0] = arr[0][i-1] + arr[1][i]
        dp[1][i][1] = arr[0][i] + arr[1][i]
    else:
        dp[1][i][0] = arr[0][i-1] + arr[1][i]
        dp[1][i][1] = arr[0][i] + arr[1][i]
        dp[1][i][2] = arr[0][i+1] + arr[1][i]

for i in range(2, n):
    for j in range(m):
        if j == 0:
            dp[i][j][1] = dp[i-1][j][2] + arr[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][:2]) + arr[i][j]
        elif j == m-1:
            dp[i][j][0] = min(dp[i-1][j-1][1:]) + arr[i][j]
            dp[i][j][1] = dp[i-1][j][0] + arr[i][j]
        else:
            dp[i][j][0] = min(dp[i-1][j-1][1:]) + arr[i][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][:2]) + arr[i][j]

answer = 1e9
for i in dp[-1]:
    answer = min(answer, min(i))

print(answer)