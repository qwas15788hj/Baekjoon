def solution(board):
    answer = 1
    
    count_o = 0 # O 개수
    count_x = 0 # X 개수
    win_o = 0 # o가 이긴 횟수
    win_x = 0# x가 이긴 횟수
    
    # 보드판 O와 X 개수 구하기
    for i in board:
        count_o += i.count("O")
        count_x += i.count("X")
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]: # 세로가 다 같다면
            if board[0][i] == "O": # O면 
                win_o += 1 # O 승리 증가
            if board[0][i] == "X": # X면
                win_x += 1 # x 승리 증가
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:# 가로가 다 같다면
            if board[i][0] == "O": # O면
                win_o += 1 # O 승리 증가
            if board[i][0] == "X": # X면
                win_x += 1 # x 승리 증가
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: # 대각선 다 같다면
        if board[0][0] == "O": # O면 
            win_o += 1 # O 승리 증가
        if board[0][0] == "X": # X면
            win_x += 1 # x 승리 증가
            
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]: # 반대 대각선 다 같다면
        if board[0][2] == "O": # O면 
            win_o += 1 # O 승리 증가
        if board[0][2] == "X": # X면
            win_x += 1 # x 승리 증가
    
    if count_x > count_o: # x 가 o 보다 많으면
        answer = 0
    if abs(count_o - count_x) > 1: # o와 x의 차이가 1보다 크면
        answer = 0
    if win_o > 0 and win_x > 0: # 둘 다 승리했으면
        answer = 0
    if win_o > 0 and count_o == count_x: # o가 승리했는데 o와 x의 개수가 같으면
        answer = 0
    if win_x > 0 and count_o != count_x: # x가 승리했는데 o와 x의 개수가 다르면
        answer = 0
    
    return answer