import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
check = ["a", "n", "t", "i", "c"]
alpha = []
for i in range(97, 97+26):
    if chr(i) not in check:
        alpha.append(chr(i))

arr = []
for _ in range(n):
    s = input()
    word = ""
    for i in range(4, len(s)-4):
        if s[i] not in check:
            word += s[i]
    arr.append(word)

if k < 5:
    print(0)
else:
    answer = 0
    for comb in list(combinations(alpha, k-5)):
        count = 0
        for i in range(len(arr)):
            flag = True
            for j in range(len(arr[i])):
                if arr[i][j] not in comb:
                    flag = False
                    break
            if flag:
                count += 1

        answer = max(answer, count)

    print(answer)