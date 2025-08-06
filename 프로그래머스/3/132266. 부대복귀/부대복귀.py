from collections import deque

def solution(n, roads, sources, destination):
    answer = [0] * (len(sources))
    
    arr = [[] for _ in range(n+1)]
    for a, b in roads:
        arr[a].append(b)
        arr[b].append(a)
    
    queue = deque()
    queue.append(destination)
    visited = [-1] * (n+1)
    visited[destination] = 0
    while queue:
        x = queue.popleft()
        for nx in arr[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    
    for i in range(len(sources)):
        answer[i] = visited[sources[i]]
    
    return answer