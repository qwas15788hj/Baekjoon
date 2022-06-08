import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_num = [0]

num = 0
for i in arr:
    num += i
    prefix_num.append(num)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_num[j]-prefix_num[i-1])