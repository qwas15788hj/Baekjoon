import math

n, s = map(int, input().split())
arr = list(map(int, input().split()))

check = []
for i in range(n):
    check.append(abs(arr[i]-s))

answer = check[0]
for i in range(1, n):
    answer = math.gcd(answer, check[i])

print(answer)