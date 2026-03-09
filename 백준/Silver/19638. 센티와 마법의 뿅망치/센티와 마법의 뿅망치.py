from heapq import heappush, heappop

n, h, t = map(int, input().split())
arr = [int(input()) for _ in range(n)]

heap = []
for i in range(n):
    heappush(heap, -arr[i])

answer = 0
for _ in range(t):
    num = -heap[0]
    if num == 1:
        break
    if num < h:
        break

    num = -heappop(heap)
    num = num//2
    heappush(heap, -num)
    answer += 1

num = -heap[0]
if num < h:
    print("YES")
    print(answer)
else:
    print("NO")
    print(num)