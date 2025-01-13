import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = sum(range(1, k+1))
if n < count:
    print(-1)
elif (n-count) % k == 0:
    print(k-1)
else:
    print(k)