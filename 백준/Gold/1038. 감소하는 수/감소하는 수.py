import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

arr = [] # 감소하는 수 저장할 배열
# 1자리 ~ 10자리까지
for i in range(1, 11):
    for comb in combinations(range(10), i):
        # 조합은 오름차순으로 나오므로, 내림차순으로 뒤집어서 수를 만듦
        com = sorted(comb, reverse=True)
        num = int(''.join(map(str, com)))
        arr.append(num)
# 정렬
arr.sort()

if n >= len(arr):
    print(-1)
else:
    print(arr[n])