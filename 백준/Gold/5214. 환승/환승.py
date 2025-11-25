import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())
arr = [[] for _ in range(n+m+1)]
station = []
for i in range(m):
    st = list(map(int, input().split()))
    station.append(st)
    for j in range(k):
        arr[st[j]].append(n+i+1)
        arr[n+i+1].append(st[j])

queue = deque()
queue.append(1)
visited_station = [0] * (n+1)
visited_tube = [0] * (n+m+1)
visited_station[1] = 1

while queue:
    x = queue.popleft()
    if x == n:
        break
    elif x < n:
        for nx in arr[x]:
            if visited_tube[nx] == 0:
                visited_tube[nx] = visited_station[x]
                queue.append(nx)
    else:
        for nx in arr[x]:
            if visited_station[nx] == 0:
                visited_station[nx] = visited_tube[x] + 1
                queue.append(nx)

if visited_station[n] == 0:
    print(-1)
else:
    print(visited_station[n])