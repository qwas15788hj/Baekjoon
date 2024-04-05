from collections import deque

n = int(input())
idx = [i for i in range(n+1)]
arr = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+1)
answer = []

def bfs(x):
    idx_store = [x]
    arr_store = [arr[x]]
    queue = deque([])
    queue.append(x)

    while queue:
        nx = queue.popleft()
        if arr[nx] not in idx_store:
            queue.append(arr[nx])
            idx_store.append(arr[nx])
            arr_store.append(arr[arr[nx]])

    idx_store.sort()
    arr_store.sort()
    if idx_store == arr_store:
        return idx_store
    else:
        return []

for i in range(1, n+1):
    if not visited[i]:
        result = bfs(i)
        if len(result) > 0:
            for j in result:
                visited[j] = True
                answer.append(j)

answer.sort()
print(len(answer))
for a in answer:
    print(a)