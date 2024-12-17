import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
count = -1
answer = -1
for i in range(n):
    arr = list(map(int, input().split()))
    comb = list(combinations(arr, 3))
    cnt = -1
    for j in range(len(comb)):
        cnt = max(cnt, sum(comb[j]) % 10)

    if cnt >= count:
        count = cnt
        answer = i + 1

print(answer)