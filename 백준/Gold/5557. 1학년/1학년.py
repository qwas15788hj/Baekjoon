import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 각 연산마다 0~20 까지의 수를 저장할 배열
dp = [[0] * 21 for _ in range(n-1)]
dp[0][arr[0]] = 1 # 첫 시작점
# 이전 수와 '+', '-' 연산하여 범위에 있고, 수가 있는지 체크
for i in range(1, n-1):
    idx = arr[i] # 현재 체크할 수
    for j in range(21):
        # '-'로직
        if 0 <= j-idx and dp[i-1][j] != 0:
            dp[i][j-idx] += dp[i-1][j]
        # '+'로직
        if j+idx < 21 and dp[i-1][j] != 0:
            dp[i][j+idx] += dp[i-1][j]

print(dp[-1][arr[-1]])