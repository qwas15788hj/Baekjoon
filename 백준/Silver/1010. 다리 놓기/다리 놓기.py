t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [1]*(n+1)

    for i in range(1, n+1):
        dp[i] = (dp[i-1]*(m-i+1))//i

    print(dp[n])