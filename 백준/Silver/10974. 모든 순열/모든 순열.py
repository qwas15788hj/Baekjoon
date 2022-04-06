from itertools import permutations
n = int(input())
arr = [i for i in range(1, n+1)]

answer = list(permutations(arr, n))
answer.sort()

for i in answer:
    print(*i)