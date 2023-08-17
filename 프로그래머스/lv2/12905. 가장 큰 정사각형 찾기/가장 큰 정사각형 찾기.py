def solution(board):
    answer = 0
    
    n = len(board) # 세로 길이
    m = len(board[0]) # 가로 길이
    arr = [[0] * (m+1) for _ in range(n+1)] # 세로 길이, 가로 길이 각각 +1 한 배열 생성 (DP 사용)
    
    for i in range(1, n+1): # 생성된 arr 배열 인덱스에 맞춰 모두 돌면서
        for j in range(1, m+1):
            if board[i-1][j-1] == 0: # 현재 값이 0 이면
                arr[i][j] = 0 # 배열도 0으로
            else: # 현재 값이 1 이면
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1 # 가로, 세로, 대각선 이전 값 중 작은 값 + 1
    
    # 배열 중 가장 큰 값 고르기
    for i in range(len(arr)):
        answer = max(answer, max(arr[i]))
    
    return answer ** 2