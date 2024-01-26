from collections import deque

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1

answer = 1e9
queue = deque()
queue.append([a, 0])
visited = [False] * n
visited[a] = True

while queue:
    idx, count = queue.popleft()
    if idx == b:
        answer = min(answer, count)
    else:
        for i in range(idx, n, arr[idx]):
            if not visited[i]:
                queue.append([i, count + 1])
                visited[i] = True

        for i in range(idx, -1, -arr[idx]):
            if not visited[i]:
                queue.append([i, count + 1])
                visited[i] = True

if answer == 1e9:
    print(-1)
else:
    print(answer)