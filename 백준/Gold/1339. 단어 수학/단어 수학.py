import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

# 알파벳 별 가중치 체크
weight = [0] * 26
for x in arr:
    x = x[::-1]
    for i in range(len(x)):
        idx = ord(x[i]) - 65
        weight[idx] += 10**i

# 가중치를 기준으로 높은 순대로 높은 번호 부여
num, max_wei = 9, 0
alpha = [-1] * 26
while True:
    max_wei = max(weight)
    if max_wei == 0:
        break

    idx = weight.index(max_wei)

    alpha[idx] = num
    weight[idx] = 0
    num -= 1

# 결과 값 출력
answer = 0
for x in arr:
    s = ""
    for i in range(len(x)):
        s += str(alpha[ord(x[i])-65])
    answer += int(s)

print(answer)