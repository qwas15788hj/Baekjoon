# dfs 함수 생성 (배열, n, 현재 체크할 row)
def dfs(queen, n, row):
    count = 0
    
    # 현재 체크할 줄이 n이면 성공
    if row == n:
        return 1
    
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col # row줄, col 열에 퀸 생성
        
        for x in range(row):
            # 세로로 겹치면 실패
            if queen[x] == queen[row]:
                break
            # 대각선으로 같으면 실패
            if abs(queen[x] - queen[row]) == row - x:
                break
        else:
            count += dfs(queen, n, row + 1) # 다음 줄 체크
            
    return count
    

def solution(n):
    return dfs([0] * n, n, 0)