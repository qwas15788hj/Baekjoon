n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
dp = [100001] * (k+1)
dp[0] = 0

for i in range(n):
    for j in range(arr[i], k+1):
        dp[j] = min(dp[j], dp[j-arr[i]] + 1)
        
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])