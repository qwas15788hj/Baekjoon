from heapq import heappush, heappop

n = int(input())
arr = []
for _ in range(n):
    heappush(arr, int(input()))

answer = 0
while len(arr) != 1:
    card = heappop(arr) + heappop(arr)
    answer += card
    heappush(arr, card)

print(answer)