import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

count = [0] * (max(arr)+1)
for i in range(m):
    for j in range(1, arr[i]+1):
        count[j] += 1

price, total = 0, 0
for i in range(1, len(count)):
    if min(count[i], n) * i > total:
        price = i
        total = min(count[i], n) * i

print(price, total)