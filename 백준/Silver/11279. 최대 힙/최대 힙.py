import sys, heapq
heap = []
n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline()) * -1
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap, a)