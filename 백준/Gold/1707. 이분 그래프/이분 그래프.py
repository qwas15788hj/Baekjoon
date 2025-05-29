import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    flag = True
    queue = deque([])
    visited = [0] * (v+1)
    for i in range(1, v+1):
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            while queue:
                if not flag:
                    break

                x = queue.popleft()
                for nx in arr[x]:
                    if visited[nx] == 0:
                        queue.append(nx)
                        visited[nx] = visited[x]%2+1
                    else:
                        if visited[nx] == visited[x]:
                            flag = False

    if flag:
        print("YES")
    else:
        print("NO")