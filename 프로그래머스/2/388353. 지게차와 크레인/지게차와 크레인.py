from collections import deque

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 컨테이너 출고 여부 확인, 바깥쪽은 방문 성공 처리
    check = [[False] * (m+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(m+2):
            if i == 0 or i == n+1 or j == 0 or j == m+1:
                check[i][j] = True

    # 지게차가 방문 가능한지, 바깥 부분 체크
    def bfs():
        queue = deque([[0, 0]])
        visited = [[False] * (m+2) for _ in range(n+2)] # 방문 가능한 바깥 부분인지 체크하는 배열
        visited[0][0] = True
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                # 다음 위치가 범위 안에 있으면 바깥 부분, check가 True인 방문한 곳이여야 큐에 저장
                if 0 <= nx < n+2 and 0 <= ny < m+2:
                    if check[nx][ny] and not visited[nx][ny]:
                        queue.append([nx, ny])
                    visited[nx][ny] = True
                        
        return visited

    for req in requests:
        r = req[0]
        # 지게차 사용
        if len(req) == 1:
            v = bfs()
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if storage[i-1][j-1] == r and not check[i][j] and v[i][j]:
                        check[i][j] = True
        # 크레인 사용
        else:
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if storage[i-1][j-1] == r and not check[i][j]:
                        check[i][j] = True

    for i in range(1, n+1):
        for j in range(1, m+1):
            if not check[i][j]:
                answer += 1
    
    return answer