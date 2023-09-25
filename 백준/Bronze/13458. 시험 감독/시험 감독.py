n = int(input()) # 시험장 개수 입력
arr = list(map(int, input().split())) # 응시자수 입력
b, c = map(int, input().split()) # 총감독관, 부감독관 입력

answer = 0 # 필요한 감독관 수
# 시험장 돌면서
for a in arr:
    a -= b # 총감독관 만큼 빼기
    answer += 1 # 총감독관 1명 추가
    # 그래도 남은 인원이 있다면
    if a > 0:
        answer += a // c # 부감독관 추가
        if a % c != 0: # 나머지 인원 부감독관이 관리를 위해
            answer += 1 # 부감독관 1명 추가

print(answer)