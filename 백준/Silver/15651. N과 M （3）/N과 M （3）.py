import sys
from itertools import product

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = list(product(arr, repeat=m))

for i in result:
    print(*i)