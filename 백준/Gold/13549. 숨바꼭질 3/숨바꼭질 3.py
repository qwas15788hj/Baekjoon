from collections import deque

n, k = map(int, input().split())

arr = [-1] * 100001
queue = deque([n])
arr[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(arr[k])
        break

    if 0 <= x*2 < 100001 and arr[x*2] == -1:
        queue.appendleft(x*2)
        arr[x*2] = arr[x]
    if 0 <= x-1 < 100001 and arr[x-1] == -1:
        queue.append(x-1)
        arr[x-1] = arr[x] + 1
    if 0 <= x+1 < 100001 and arr[x+1] == -1:
        queue.append(x+1)
        arr[x+1] = arr[x] + 1