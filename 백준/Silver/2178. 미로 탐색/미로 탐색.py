from collections import deque

# 입력받기
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 이동 방향 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global result  # 전역 변수 result 사용
    q = deque()
    q.append((x, y))
    grid[x][y] = 0  # 시작점 방문 처리
    result = 1  # 시작점 포함 경로 길이 초기화
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            if x == n-1 and y == m-1:
                return result
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    grid[nx][ny] = 0

        result += 1


print(bfs(0, 0))