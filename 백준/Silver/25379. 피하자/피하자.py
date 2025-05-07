import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

odd, odd_cnt = 0, 0
even, even_cnt = 0, 0
for i in range(n):
    if arr[i] % 2 != 0:
        odd += abs(i-odd_cnt)
        odd_cnt += 1
    else:
        even += abs(i-even_cnt)
        even_cnt += 1

print(min(odd, even))