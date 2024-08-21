import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] == 1:
        queue.appendleft(s[1])
    elif s[0] == 2:
        queue.append(s[1])
    elif s[0] == 3:
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif s[0] == 4:
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif s[0] == 5:
        print(len(queue))
    elif s[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 7:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 8:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)