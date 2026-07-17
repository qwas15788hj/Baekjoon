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
        
        # 0 ~ n-1까지 방문 가능한 곳 찾기
        for nx in range(n):
            # 조건1 : 아직 방문 안한 곳
            if not (mask & (1<<nx)):
                # 조건2 : 부모가 방문한 곳이여야 함 (0제외)
                if nx == 0 or (mask & (1<<parent[nx])):
                    nmask = mask | (1<<nx)
                    if info[nx] == 0:
                        queue.append([nx, nmask, s+1, w])
                        visited[nx][nmask] = True
                    elif info[nx] == 1 and s > w+1:
                        queue.append([nx, nmask, s, w+1])
                        visited[nx][nmask] = True
        
    return answer