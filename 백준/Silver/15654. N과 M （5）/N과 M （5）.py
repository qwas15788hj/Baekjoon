from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
li = list(permutations(arr, m))
li.sort()
for i in li:
    print(*i)