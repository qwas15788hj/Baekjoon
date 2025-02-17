n = int(input())
m = int(input())
arr = [1] * n
for _ in range(m):
    arr[int(input())-1] = 0

check = []
count = 0
for i in range(n):
    if arr[i] == 1:
        count += 1
    else:
        check.append(count)
        count = 0
if count != 0:
    check.append(count)
    
dp = [1] * (max(check)+1)
for i in range(1, len(dp)):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]

answer = 1
for i in range(len(check)):
    answer *= dp[check[i]]

print(answer)