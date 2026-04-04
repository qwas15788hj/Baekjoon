import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
opr = list(map(int, input().split()))

op = []
for i in range(4):
    for _ in range(opr[i]):
        op.append(i)

perm = list(permutations(op, len(op)))
answer1 = -int(1e9)
answer2 = int(1e9)
for per in perm:
    result = arr[0]
    for i in range(n-1):
        if per[i] == 0:
            result += arr[i+1]
        elif per[i] == 1:
            result -= arr[i+1]
        elif per[i] == 2:
            result *= arr[i+1]
        elif per[i] == 3:
            if result < 0 and arr[i+1] > 0:
                result = -(-result // arr[i+1])
            else:
                result //= arr[i+1]

    answer1 = max(answer1, result)
    answer2 = min(answer2, result)

print(answer1)
print(answer2)