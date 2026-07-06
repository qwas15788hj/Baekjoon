from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        n, m = len(grid), len(grid[0])
        sz, sy, k = 0, 0, 0
        for i in range(n):
            for j in range(m):
                if 97 <= ord(grid[i][j]) <= 122:
                    k += 1
                if grid[i][j] == '@':
                    sx, sy = i, j
        
        queue = deque([[sx, sy, '', 0]])
        visited = set()
        visited.add((sx, sy, ''))
        while queue:
            x, y, key, d = queue.popleft()
            if len(key) == k:
                return d
            
            for p in range(4):
                nx = x + dx[p]
                ny = y + dy[p]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                    # 열쇠
                    if 97 <= ord(grid[nx][ny]) <= 122:
                        nkey = "".join(sorted(set(key + grid[nx][ny])))
                        if (nx, ny, nkey) not in visited:
                            queue.append([nx, ny, nkey, d+1])
                            visited.add((nx, ny, nkey))
                    # 자물쇠
                    if 65 <= ord(grid[nx][ny]) <= 90:
                        if chr(ord(grid[nx][ny])+32) in key and (nx, ny, key) not in visited:
                            queue.append([nx, ny, key, d+1])
                            visited.add((nx, ny, key))
                    if grid[nx][ny] in ['.', '@'] and (nx, ny, key) not in visited:
                        queue.append([nx, ny, key, d+1])
                        visited.add((nx, ny, key))

        return -1