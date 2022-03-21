import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0]*100001
queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    for nx in (x-1, x+1, x*2):
        if nx >= 0 and nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x]+1
            queue.append(nx)