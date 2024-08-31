import sys
input = sys.stdin.readline
from itertools import product

result = list(map(int, input().split()))
num = [i for i in range(1, 6)]

def check(a):
    flag = True
    for i in range(8):
        if a[i] == a[i+1] and a[i+1] == a[i+2]:
            flag = False
    return flag

answer = 0
for arr in product(range(1, 6), repeat=10):
    score = 0
    if check(arr):
        for j in range(len(arr)):
            if arr[j] == result[j]:
                score += 1
        if score >= 5:
            answer += 1

print(answer)