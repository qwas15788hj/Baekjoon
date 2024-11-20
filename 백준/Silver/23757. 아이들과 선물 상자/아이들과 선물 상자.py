import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
box = list(map(int, input().split()))
child = list(map(int, input().split()))
boxH = []
for i in range(n):
    heapq.heappush(boxH, -box[i])

for i in range(m):
    now = child[i]
    gift = -heapq.heappop(boxH)
    if gift > now:
        heapq.heappush(boxH, -(gift-now))
    elif gift == now:
        continue
    else:
        print(0)
        exit()

print(1)