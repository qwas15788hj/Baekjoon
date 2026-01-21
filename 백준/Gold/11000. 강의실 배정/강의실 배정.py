import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0], x[1]))
room = []
heappush(room, arr[0][1])
for i in range(1, len(arr)):
    heappush(room, arr[i][1])
    if arr[i][0] >= room[0]:
        heappop(room)

print(len(room))