import heapq

n = int(input())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(arr) == 0:
            print(-1)
        else:
            print(-1 * heapq.heappop(arr))
    else:
        for i in range(1, a[0]+1):
            heapq.heappush(arr, -1 * a[i])