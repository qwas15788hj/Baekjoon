import heapq

n = int(input())
a = int(input())
arr = []
heapq.heappush(arr, 0)
for i in range(n-1):
    heapq.heappush(arr, -int(input()))

answer = 0
while True:
    s = heapq.heappop(arr)
    if a > -s:
        break
    a += 1
    s += 1
    answer += 1
    heapq.heappush(arr, s)

print(answer)