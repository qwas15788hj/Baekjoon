import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append([s, t])

arr.sort()

room = []
heapq.heappush(room, arr[0][1])

for i in range(1, len(arr)):
    if arr[i][0] < room[0]: #회의실 끝나는 시간보다 다음 회의 시작이 빠르면
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))