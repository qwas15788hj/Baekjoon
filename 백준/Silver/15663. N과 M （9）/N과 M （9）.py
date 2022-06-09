from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = list(permutations(arr, m))
answer = list(set(answer))
answer.sort()
for i in answer:
    print(*i)