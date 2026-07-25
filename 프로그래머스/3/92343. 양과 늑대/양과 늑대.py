from collections import deque

def solution(info, edges):
    answer = 0
    
    n, m = len(info), len(edges)
    arr = [[] for _ in range(n)]
    parent = dict()
    for a, b in edges:
        arr[a].append(b)
        parent[b] = a
    
    queue = deque([[0, 1<<0, 1, 0]])
    visited = [[False] * (1<<n) for _ in range(n)]
    visited[0][1<<0] = True
    while queue:
        x, mask, s, w = queue.popleft()
        answer = max(answer, s)
        
        for nx in range(n):
            # 아직 방문X
            if not (mask & 1<<nx):
                # 부모는 방문했어야 함 (0 제외)
                if nx == 0 or (mask & 1<<parent[nx]):
                    nmask = mask | 1<<nx
                    if info[nx] == 0:
                        queue.append([nx, nmask, s+1, w])
                        visited[nx][nmask] = True
                    elif info[nx] == 1 and s > w+1:
                        queue.append([nx, nmask, s, w+1])
                        visited[nx][nmask] = True
        
    return answer