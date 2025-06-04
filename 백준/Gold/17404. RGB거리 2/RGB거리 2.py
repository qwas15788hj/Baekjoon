import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9
for start in range(3):
    dp =[[1e9] * 3 for _ in range(n)]
    dp[0][start] = arr[0][start]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    for end in range(3):
        if start != end:
            answer = min(answer, dp[-1][end])

print(answer)