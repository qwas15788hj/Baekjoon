from itertools import permutations

n = int(input())
k = int(input())
arr = []
dic = dict()
for _ in range(n):
    arr.append(int(input()))

answer = 0
for per in permutations(arr, k):
    s = ""
    for p in per:
        s += str(p)

    if s not in dic:
        dic[s] = 1
        answer += 1

print(answer)