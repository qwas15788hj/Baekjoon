import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
arr1 = [[] for _ in range(n+1)]
arr2 = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr1[a].append(b)
    arr2[b].append(a)
    
for i in range(1, n+1):
    visited1 = [False] * (n+1)
    queue = deque([])
    queue.append(i)
    visited1[i] = True
    while queue:
        x = queue.popleft()
        for nx in arr1[x]:
            if not visited1[nx]:
                queue.append(nx)
                visited1[nx] = True

    visited2 = [False] * (n+1)
    queue = deque([])
    queue.append(i)
    visited2[i] = True
    while queue:
        x = queue.popleft()
        for nx in arr2[x]:
            if not visited2[nx]:
                queue.append(nx)
                visited2[nx] = True

    answer = 0
    for i in range(1, n+1):
        if not visited1[i] and not visited2[i]:
            answer += 1

    print(answer)