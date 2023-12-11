import math

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
sub = []
for i in range(n-1):
    sub.append(arr[i+1] - arr[i])

gcd = sub[0]
for i in range(1, len(sub)):
    gcd = math.gcd(gcd, sub[i])

answer = 0
for i in range(len(sub)):
    answer += sub[i]//gcd - 1

print(answer)