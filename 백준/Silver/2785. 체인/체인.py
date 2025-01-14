import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
queue = deque([])
for i in range(n):
    queue.append(arr[i])


answer = 0
while len(queue) != 1:
    queue[0] -= 1
    num = queue.pop()
    queue[-1] += num
    if queue[0] == 0:
        queue.popleft()

    answer += 1

print(answer)