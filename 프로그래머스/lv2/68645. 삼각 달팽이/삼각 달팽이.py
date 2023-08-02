def solution(n):
    answer = []
    arr = [[0]*i for i in range(1, n+1)] # 달팽이 배열 생성
    x, y, num = 0, 0, 1 # 세로, 가로, 현재 번호
    arr[x][y] = num # 시작점인 [0][0] 인덱스에 1 저장
    
    target = 0 # 블록 갯수
    for i in range(1, n+1): # 총 블록 개수 구하기
        target += i
        
    dx = [1, 0, -1] # 하, 우, 왼쪽 대각
    dy = [0, 1, -1]
    
    while True: # 계속 무한 반복
        for i in range(3): # 세 방향 진행
            while True: # 현재 가는 방향 몇번인지 모름으로 계속 무한 반복
                x += dx[i] # 다음 위치
                y += dy[i]
                # 다음 위치가 범위 밖이거나 이미 값이 채워졌다면
                if x >= n or x < 0 or y >= n or y < 0 or arr[x][y] != 0:
                    x -= dx[i] # 다시 이전위치로 돌아오고 while문 멈춤
                    y -= dy[i]
                    break
                else: # 범위 안이고 값이 안채워졌다면
                    num += 1 # 값 증가 후
                    arr[x][y] = num # 해당 배열에 값 저장
                    
        if num == target: # 현재 번호가 타깃 넘버와 같다면 모두 방문한 것임으로 정지
            break
    
    # 구한 달팽이 배열 answer에 순서대로 요소 저장
    for i in arr:
        for j in i:
            answer.append(j)
        
    return answer