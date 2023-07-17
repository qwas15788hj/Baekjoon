def solution(dirs):
    answer = 0
    
    visited = set() # 방문한 길 저장할 집합
    x, y = 0, 0 # 현 위치
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    move = ["U", "D", "L", "R"]
    
    for d in dirs: # 입력 반복
        idx = move.index(d) # 현재 입력 방향 인덱스
        nx = x + dx[idx] # 현재 방향을 통한 다음 방향
        ny = y + dy[idx]
        if -5 <= nx <= 5 and -5 <= ny <= 5: # 다음 방향이 범위안에 있다면
            if (x, y, nx, ny) not in visited: # (현위치, 다음위치) 가 집합에 없다면
                visited.add((x, y, nx, ny)) # 집합에 (현위치, 다음위치) 추가 / 현재 -> 다음
                visited.add((nx, ny, x, y)) # 집합에 (다음위치, 현위치) 추가 / 다음 -> 현재 (반대로 오는 방향)
                answer += 1 # + 1
            x, y = nx, ny # 현 위치 갱신 / 두 번째 if문 절에 넣으면 방문했다면 갱신이 안됨으로 2개의 if 문을 사용하고, 첫 번째 if문 절에
    
    return answer