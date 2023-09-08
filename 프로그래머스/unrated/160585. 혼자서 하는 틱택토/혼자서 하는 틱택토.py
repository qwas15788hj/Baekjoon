def solution(board):
    answer = 1 # 초기 성공한다는 가정하에 1로 설정
    
    count_o = 0 # O의 개수
    count_x = 0 # X의 개수
    win_o = 0 # O가 이긴 횟수
    win_x = 0 # X가 이긴 횟수
    
    # O와 X 개수 구하기
    for i in board:
        count_o += i.count("O")
        count_x += i.count("X")
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]: # 세로가 다 같다면
            if board[0][i] == "O": # 해당 위치가 O면
                win_o += 1 # O 승리
            if board[0][i] == "X": # 해당 위치가 X면
                win_x += 1 # X 승리
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]: # 가로가 다 같다면
            if board[i][0] == "O": # 해당 위치가 O면
                win_o += 1 # O 승리
            if board[i][0] == "X": # 해당 위치가 X면
                win_x += 1 # X 승리
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: # 대각선 체크
        if board[0][0] == "O": # 해당 위치가 O면
                win_o += 1 # O 승리
        if board[0][0] == "X": # 해당 위치가 X면
            win_x += 1 # X 승리
            
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]: # 반대 대각선 체크
        if board[0][2] == "O": # 해당 위치가 O면
                win_o += 1 # O 승리
        if board[0][2] == "X": # 해당 위치가 X면
            win_x += 1 # X 승리
    
    # 나올 수 있는 상황인지 체크
    if count_x > count_o: # X가 O보다 많으면 실패
        answer = 0
    if abs(count_o - count_x) > 1: # 두 개의 개수 차이가 1보다 크면 실패
        answer = 0
    if win_o > 0 and win_x > 0: # 둘다 승리가 있다면 실패
        answer = 0
    if win_o > 0 and count_o == count_x: # O가 이겼는데 두 개의 개수가 같다면 실패
        answer = 0
    if win_x > 0 and count_o != count_x: # X가 이겼는데 두 개의 개수가 다르다면 실패
        answer = 0
    
    return answer