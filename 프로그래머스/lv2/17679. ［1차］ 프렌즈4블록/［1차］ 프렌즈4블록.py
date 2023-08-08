def solution(m, n, board):
    answer = 0
    
    arr = [list(board[i]) for i in range(m)] # board를 리스트 형태로 변경
    
    dx = [0, 1, 0, 1] # 현재 위치, 아래, 오른쪽, 오른쪽 아래
    dy = [0, 0, 1, 1]
    
    while True: # 무한 반복
        remove = [] # 제거할 블록의 맨왼쪽 위의 위치를 저장할 배열
        for i in range(m - 1): # 블록을 모두 돌면서
            for j in range(n - 1):
                # 해당 블록이 X가 아닌 문자이며 오른쪽, 아래, 오른쪽 아래가 모두 같을 경우
                if arr[i][j] != "X" and arr[i][j] == arr[i+1][j] and arr[i][j] == arr[i][j+1] and arr[i][j] == arr[i+1][j+1]:
                        remove.append([i, j]) # 배열에 저장

        if len(remove) == 0: # 제거할 블록이 없으면 무한 루프 종료
            break

        # 블록 모두 확인이 끝난 후 제거할 블록이 있다면
        for i, j in remove: # 제거할 블록 위치를 통해
            for z in range(4): # 현재 블록 네 방향 탐색
                x, y = i + dx[z], j + dy[z] # 현재 블록
                if arr[x][y] != "X": # 현재 블록이 X가 아니면 
                    answer += 1 # answer 증가
                arr[x][y] = "X" # 현재 블록 X로 변경

        # 빈 블록 채우기
        for i in range(n): # 가로 모두 확인
            for j in range(m - 1, -1, -1): # 맨 밑 바로 위부터 맨 위까지 확인
                if arr[j][i] == "X": # 해당 위치가 빈 배열이면
                    for z in range(j - 1, -1, -1): # 그 위치 바로 위부터 맨 위까지 탐색
                        if arr[z][i] != "X": # 해당 위치가 빈 배열이 아니면
                            arr[j][i], arr[z][i] = arr[z][i], "X" # 두 위치를 변경 후
                            break # 빈 배열 아닌 문자 찾는 for문 종료
    
    return answer