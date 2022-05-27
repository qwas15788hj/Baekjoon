from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))
li = list(product(arr, repeat=m))
li.sort()
for i in li:
    print(*i)