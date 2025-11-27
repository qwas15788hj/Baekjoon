import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
bag = []
for _ in range(k):
    bag.append(int(input()))

jewel.sort(key=lambda x:x[0])
bag.sort()

arr = []
idx = 0
answer = 0
for weight in bag:
    while idx < n and jewel[idx][0] <= weight:
        heappush(arr, -jewel[idx][1])
        idx += 1

    if arr:
        answer += -heappop(arr)

print(answer)