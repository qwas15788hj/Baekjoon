import sys
input = sys.stdin.readline
from itertools import product

a, b = map(int, input().split())
x, y = len(str(a)), len(str(b))
count = 0
for i in range(x, y+1):
    pro = list(product([4, 7], repeat=i))
    for p in pro:
        n = int(''.join(map(str, p)))
        if a <= n <= b:
            count += 1

print(count)