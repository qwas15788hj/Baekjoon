import heapq

n = int(input())
s = list(map(int, input().split()))
answer = 0
arr = []
for i in s:
    heapq.heappush(arr, -i)

while len(arr) >= 2:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    a += 1
    b += 1
    if a != 0:
        heapq.heappush(arr, a)
    if b != 0:
        heapq.heappush(arr, b)
    answer += 1

if len(arr):
    answer += abs(arr[0])

if answer > 1440:
    print(-1)
else:
    print(answer)