from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9

for s in range(n):
    queue = deque([])
    queue.append([s, 0, [s]])

    while queue:
        x, cost, v = queue.popleft()
        if len(v) == n:
            if arr[x][s] != 0:
                answer = min(answer, cost + arr[x][s])
        else:
            if cost < answer:
                for i in range(n):
                    if arr[x][i] != 0 and i not in v:
                        queue.append([i, cost+arr[x][i], v+[i]])

print(answer)