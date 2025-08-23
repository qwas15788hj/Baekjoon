from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:x[1])
queue = []
for pay, day in arr:
    heappush(queue, pay)
    if day < len(queue):
        heappop(queue)

print(sum(queue))