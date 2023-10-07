n = int(input()) # n 입력
arr = list(map(int, input().split())) # 자동차 번호 입력
answer = 0
for a in arr: # 리스트 돌면서
    if a == n: # 자동차 번호가 n 과 같다면
        answer += 1 # answer 증가

print(answer)