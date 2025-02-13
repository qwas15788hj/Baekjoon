n, s, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            n1 = j + arr[i]
            n2 = j - arr[i]
            if n1 <= m:
                dp[i+1][n1] = 1
            if n2 >= 0:
                dp[i+1][n2] = 1

answer = -1
for i in range(m+1):
    if dp[n][i] == 1:
        answer = max(answer, i)

print(answer)