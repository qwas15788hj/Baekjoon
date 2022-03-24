from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    answer = 0
    
    for x, y in enumerate(arr):
        queue.append([x, y])
    
    while True:
        for i in range(1, len(queue)):
            if queue[0][1] < queue[i][1]:
                queue.append(queue.popleft())
                break
        else:
            x = queue.popleft()
            answer += 1
            if x[0] == m:
                print(answer)
                break