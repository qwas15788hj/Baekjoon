n = int(input()) # 이동해야 할 채널
m = int(input()) # 고장난 버튼 개수
if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

answer = abs(100 - n) # 처음은 채널이 100이기에 시작 채널과 이동해야할 채널 차이를 answer로 설정
for channel in range(1000001): # 최대 50만까지기에 0~50만을 넘어서 예외처리를 위해 1000001로 설정
    flag = True
    for ch in str(channel): # 현재 채널의 번호를 돌며
        if int(ch) in arr: # 현재 번호가 고장난 버튼이라면
            flag = False # 누를 수 없음
            break

    if flag: # 누를 수 있는 버튼이라면
        # 현재 answer와 현재 채널의 길이와 채널 - 현재 채널의 차이 중 작은 값 선택
        answer = min(answer, len(str(channel)) + abs(channel - n))

print(answer)