import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for a in arr:
    a.sort(reverse=True)

def dfs(t):
    global cnt
    visited[t] = cnt
    for x in arr[t]:
        if not visited[x]:
            cnt += 1
            dfs(x)

cnt = 1
dfs(r)
for i in range(1, len(visited)):
    print(visited[i])