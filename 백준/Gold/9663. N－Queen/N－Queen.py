import sys
input = sys.stdin.readline

n = int(input())

answer = 0
row = [0] * n

# 세로가 다르고, 대각선이 다른지 체크
def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queen(x):
    global answer

    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            # [x, i] 지점에 퀸 생성
            row[x] = i
            if check(x): # 체크 성공하면
                n_queen(x+1) # 다음 줄로 이동

n_queen(0)
print(answer)