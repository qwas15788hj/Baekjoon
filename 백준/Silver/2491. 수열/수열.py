n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1

arr = arr[::-1]
dp_rev = [0] * n
dp_rev[0] = 1
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp_rev[i] = dp_rev[i-1] + 1
    else:
        dp_rev[i] = 1

print(max(max(dp), max(dp_rev)))