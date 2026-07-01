from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
            
        n = len(grid)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 각 지점 별 도둑과의 거리
        queue = deque([])
        dist = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    dist[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1
        
        # 가능한 거리인지 체크
        def check(d):
            if dist[0][0] < d or dist[-1][-1] < d:
                return False
            
            queue = deque([[0, 0]])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            while queue:
                x, y = queue.popleft()
                if x == n-1 and y == n-1:
                    return True
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= d:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
            
            return False
        
        
        # 이분탐색으로 거리 측정
        answer = 0
        start, end = 0, n
        while start <= end:
            mid = (start + end)//2
            if check(mid):
                answer = mid
                start = mid + 1
            else:
                end = mid - 1

        return answer