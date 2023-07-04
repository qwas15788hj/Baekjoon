def solution(progresses, speeds):
    answer = []
    stack = [0] * len(progresses) # 몇 일 걸리는지 저장하는 스택
    for i in range(len(progresses)): # 프로그래스 반복
        day = (100 - progresses[i]) // speeds[i] # 몇일걸리는지 계산
        if progresses[i] + day * speeds[i] < 100: # 계산에서 나온 day만큼 계산했는데 100보다 작으면
            day += 1 # 1일 추가
        stack[i] = day # day 값 저장
    
    now = stack[0] # 현재 요일 = 처음 걸리는 요일로 선언
    num = 1 # 개수 1로 선언
    for i in range(1, len(stack)): # 1 ~ 스택 길이만큼 반복
        if stack[i] <= now: # 이전의 값이 현재 스택의 요소보다 크거나 같으면
            num += 1 # 한꺼번에 가능함으로 num 증가
        else: # 현재 스택이 이전의 값보다 크면
            now = stack[i] # now 초기화
            answer.append(num) # answer에 num 저장
            num = 1 # num 1로 초기화
    answer.append(num) # 마지막 num이 저장이 안됨으로 예외처리

    return answer