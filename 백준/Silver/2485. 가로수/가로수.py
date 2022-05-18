def gcd(x, y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

n = int(input())
tree = []
arr = []
for _ in range(n):
    tree.append(int(input()))

for i in range(n-1):
    arr.append(tree[i+1]-tree[i])

dp = [0]*(n-2)
dp[0] = gcd(arr[0], arr[1])
for i in range(1, n-2):
    dp[i] = gcd(dp[i-1], arr[i+1])

gcd_num = dp[-1]
count = 0
for i in arr:
    count += (i//gcd_num)-1

print(count)