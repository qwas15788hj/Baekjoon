import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int, input().split())

queue = []
heappush(queue, [0, s])
visited = [1e9] * (n+1)
visited[s] = 0
target = [[] for _ in range(n+1)]
while queue:
    c, x = heappop(queue)
    if x == e:
        break

    for nx, nc in arr[x]:
        if visited[nx] > c + nc:
            heappush(queue, [c+nc, nx])
            visited[nx] = c + nc
            target[nx] = [x]

answer = [e]
x = e
while True:
    nx = target[x][0]
    answer.append(nx)
    x = nx
    if nx == s:
        break
    
print(visited[e])
print(len(answer))
print(*answer[::-1])