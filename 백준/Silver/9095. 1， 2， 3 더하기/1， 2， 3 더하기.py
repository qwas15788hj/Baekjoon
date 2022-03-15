t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0]*10
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n-1])