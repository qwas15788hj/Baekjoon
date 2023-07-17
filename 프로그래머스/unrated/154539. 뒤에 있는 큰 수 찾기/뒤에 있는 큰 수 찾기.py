def solution(numbers):
    answer = [0] * len(numbers)
    
    stack = [] # 스택 생성
    for i in range(len(numbers)):
        if len(stack) == 0: # 스택이 비었으면
            stack.append(i) # 현재 인덱스 번호 넣기
        else: # 스택에 요소가 있다면
            # 현재 인덱스 번호에 해당하는 번호가 스택 맨 위의 인덱스에 해당하는 번호보다 크면
            while numbers[i] > numbers[stack[-1]]:
                answer[stack.pop()] = numbers[i] # 스택 맨 위의 인덱스에 현재 number 값으로 선언
                if len(stack) == 0: # 스택이 비었으면 멈춤
                    break
            stack.append(i) # 스택에 인덱스 번호 넣기
    
    while stack: # 스택에 요소가 있다면
        answer[stack.pop()] = -1 # 스택 요소에 -1 입력
    
    return answer