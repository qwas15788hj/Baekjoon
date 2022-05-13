from collections import deque

n, k = map(int, input().split())
visited = [0]*(100001)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v])
            break
        for i in (v-1, v+1, v*2):
            if i >= 0 and i <= 100000 and visited[i] == 0:
                visited[i] = visited[v]+1
                queue.append(i)

bfs(n)