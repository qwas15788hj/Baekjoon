from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
result = [0] * 2000001

for i in range(1, n+1):
    comb = list(combinations(arr, i))
    for com in comb:
        result[sum(com)] = 1

for i in range(1, len(result)):
    if result[i] == 0:
        print(i)
        break