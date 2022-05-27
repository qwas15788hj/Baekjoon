from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
li = list(combinations_with_replacement(arr, m))
li.sort()
for i in li:
    print(*i)