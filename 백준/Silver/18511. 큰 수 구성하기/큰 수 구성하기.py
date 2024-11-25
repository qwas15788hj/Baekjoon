import sys
input = sys.stdin.readline
from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
pro = list(product(arr, repeat=len(str(n)))) + list(product(arr, repeat=len(str(n))-1))
for i in pro:
    num = int("".join(map(str, i)))
    if n >= num:
        answer = max(answer, num)

print(answer)