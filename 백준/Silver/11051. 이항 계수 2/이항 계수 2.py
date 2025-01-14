import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = 1
for i in range(k):
    answer *= (n-i)

for i in range(1, k+1):
    answer //= i

print(answer%10007)