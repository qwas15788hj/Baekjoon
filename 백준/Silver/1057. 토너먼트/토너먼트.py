import sys
input = sys.stdin.readline

n, a, b = map(int, input().split()) # 입력

# 큰 값이 b가 되도록
if a > b:
    a, b = b, a

answer = 0 # 몇라운드 했는지
while True:
    answer += 1 # 다음 라운드
    # a(작은값)가 홀수고, b(큰값)가 짝수고 둘의 차가 1이면 종료
    if a % 2 != 0 and b % 2 == 0 and b - a == 1:
        break
    a = (a+1) // 2 # 다음 라운드 a의 값
    b = (b+1) // 2 # 다음 라운드 b의 값

print(answer)