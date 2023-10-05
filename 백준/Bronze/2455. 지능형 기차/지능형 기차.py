answer = 0 # 최대 사람 수 저장
count = 0 # 현재 사람 수
for _ in range(4): # 4개 역 반복
    a, b = map(int, input().split()) # 내린 사람, 탄 사람 입력
    count += (b - a) # 현재 사람 수에 + 탄 사람 - 내린 사람
    answer = max(answer, count) # 최대 사람 수 갱신

print(answer)