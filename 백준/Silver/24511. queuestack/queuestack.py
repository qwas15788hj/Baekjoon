import sys
from collections import deque

n = int(input())
data = list(map(int, input().split()))
arr = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

queue = deque()
for i in range(n):
    if data[i] == 0:
        queue.appendleft(arr[i])

for i in range(m):
    queue.append(num[i])
    print(queue.popleft(), end=" ")