import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
arr = list(map(str, input().split()))

answer = []
alpha = ["a", "e", "i", "o", "u"]
comb = list(combinations(arr, l))
for com in comb:
    cnt1, cnt2 = 0, 0
    for i in range(len(com)):
        if com[i] in alpha:
            cnt1 += 1
        else:
            cnt2 += 1

    if cnt1 >= 1 and cnt2 >= 2:
        answer.append("".join(sorted(com)))

answer.sort()
for i in answer:
    print(i)