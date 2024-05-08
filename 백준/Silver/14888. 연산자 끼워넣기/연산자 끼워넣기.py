import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
op_arr = []
for i in range(len(op)):
    for j in range(op[i]):
        op_arr.append(i)

max_answer = -int(1e9)
min_answer = int(1e9)
for per in list(permutations(op_arr, len(op_arr))):
    num = arr[0]
    for i in range(n-1):
        if per[i] == 0:
            num += arr[i+1]
        elif per[i] == 1:
            num -= arr[i+1]
        elif per[i] == 2:
            num *= arr[i+1]
        elif per[i] == 3:
            if num < 0 and arr[i+1] > 0:
                num = -1 * (num*(-1) // arr[i+1])
            else:
                num //= arr[i+1]

    max_answer = max(max_answer, num)
    min_answer = min(min_answer, num)

print(max_answer)
print(min_answer)