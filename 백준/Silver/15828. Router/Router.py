from collections import deque

n = int(input())
queue = deque([])
while True:
    s = int(input())
    if s == -1:
        if queue:
            print(*queue)
        else:
            print("empty")
        break

    if s == 0 and queue:
        queue.popleft()
    if s > 0 and len(queue) < n:
        queue.append(s)