from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
li = list(combinations(arr, m))
li.sort()
for i in li:
    print(*i)