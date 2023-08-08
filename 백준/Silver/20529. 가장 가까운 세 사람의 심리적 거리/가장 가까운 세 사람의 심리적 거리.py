t = int(input()) # 테스트케이스 입력
for _ in range(t): # t 반복
    answer = 1e9
    n = int(input()) # n 입력
    arr = list(map(str, input().split())) # MBTI 입력

    if n > 32: # n이 33 이상이면 MBTI가 16개 임으로 무조건 3개가 되는 것이 있으므로 0
        print(0)
    else:
        # 삼중 for문 사용하여 세명 고르기
        for i in range(n):
            for j in range(n):
                for z in range(n):
                    count = 0
                    if i == j or j == z or i == z: # 각기 다른 사람을 골라야하는데 두명이 겹치면
                        continue # 무시
                    for k in range(4): # MBTI 4개를 하나씩 체크
                        if arr[i][k] != arr[j][k]: # 1번 사람과 2번 사람의 MBTI 요소가 다르면
                            count += 1 # 카운트 증가
                        if arr[j][k] != arr[z][k]: # 2번 사람과 3번 사람의 MBTI 요소가 다르면
                            count += 1 # 카운트 증가
                        if arr[i][k] != arr[z][k]: # 1번 사람과 3번 사람의 MBTI 요소가 다르면
                            count += 1 # 카운트 증가

                    # 고른 세 명의 MBTI 4가지 모두 체크 시
                    answer = min(answer, count) # 최소 값으로 갱신

        print(answer)