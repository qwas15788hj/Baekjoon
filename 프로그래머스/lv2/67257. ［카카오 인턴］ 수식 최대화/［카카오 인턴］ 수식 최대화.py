from itertools import permutations

# 연산자를 통해 연산해주는 함수
def calcu(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b
    
def solution(expression):
    answer = 0
    
    operation = ["+", "-", "*"] # 모든 연산자
    arr = [] # 처음에 연산자를 기준으로 원소를 나눌 배열
    num = "" # 원소가 연산자가 아닐때 저장할 문자열
    for i in expression: # 원소를 돌면서
        if i == "+" or i == "-" or i == "*": # 원소가 연산자면
            arr.append(int(num)) # 배열에 저장한 숫자 넣고
            arr.append(i) # 연산자 넣기
            num = "" # 숫자 초기화
        else: # 원소가 연산자가 아니면
            num += str(i) # 숫자에 더하기
    arr.append(int(num)) # 마지막 숫자 배열에 넣기
    
    for op in list(permutations(operation, 3)): # + - *
        for i in range(len(op)): # 0, 1, 2
            if i == 0: # 첫번째
                stack = [] # 첫번째 스택
                flag = False # 체크
                for j in range(len(arr)): # 배열 돌면서
                    if flag == True: # 체크면 밑에
                        flag = False # 체크 풀고
                        continue # 밑 연산 무시
                    if arr[j] == op[i]: # 현재 우선순위에 맞는 연산자면
                        # 연산자에 맞게 끔 연산해주는 함수를 통해 스택에 넣기
                        stack.append(calcu(stack.pop(), arr[j+1], arr[j]))
                        flag = True # 체크
                    else: # 아니면
                        stack.append(arr[j]) # 스택에 넣기
            elif i == 1:
                stack2 = []
                flag = False # 체크
                for j in range(len(stack)): # 배열 돌면서
                    if flag == True: # 체크면 밑에
                        flag = False # 체크 풀고
                        continue # 밑 연산 무시
                    if stack[j] == op[i]: # 현재 우선순위에 맞는 연산자면
                        # 연산자에 맞게 끔 연산해주는 함수를 통해 스택에 넣기
                        stack2.append(calcu(stack2.pop(), stack[j+1], stack[j]))
                        flag = True # 체크
                    else: # 아니면
                        stack2.append(stack[j]) # 스택에 넣기
            else:
                stack3 = []
                flag = False # 체크
                for j in range(len(stack2)): # 배열 돌면서
                    if flag == True: # 체크면 밑에
                        flag = False # 체크 풀고
                        continue # 밑 연산 무시
                    if stack2[j] == op[i]: # 현재 우선순위에 맞는 연산자면
                        # 연산자에 맞게 끔 연산해주는 함수를 통해 스택에 넣기
                        stack3.append(calcu(stack3.pop(), stack2[j+1], stack2[j]))
                        flag = True # 체크
                    else: # 아니면
                        stack3.append(stack2[j]) # 스택에 넣기
                        
        answer = max(answer, abs(stack3[0])) # 스택3에 있는 최종 값의 절대 값과 비교하여 큰 값으로 변경
        
    return answer