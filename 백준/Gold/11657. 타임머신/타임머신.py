import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

if len(arr[1]) == 0:
    for i in range(2, n+1):
        print(-1)
    exit()

dist = [1e9] * (n+1)
dist[1] = 0
for _ in range(n-1):
    for x in range(1, n+1):
        for nx, c in arr[x]:
            if dist[x] + c < dist[nx]:
                dist[nx] = dist[x] + c

flag = True
for x in range(1, n+1):
    for nx, c in arr[x]:
        if dist[x] + c < dist[nx]:
            flag = False

if flag:
    for i in range(2, n+1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)