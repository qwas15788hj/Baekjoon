from collections import deque

def solution(s):
    answer = 0
    queue = deque(s) # s를 큐로 변환
    
    for i in range(len(s)): # s길이만큼 반복
        queue.append(queue.popleft()) # 큐의 맨 앞을 맨 뒤로 이동
        stack = [] # 괄호 저장할 스택 선언
        for j in range(len(queue)): # 큐 길이만큼 반복
            if len(stack) == 0: # 스택이 비었으면
                stack.append(queue[j]) # 현재 괄호 스택에 저장
            else: # 스택에 요소가 있다면
                # 스택의 맨 끝과 현재 괄호 모양을 비교하여 서로 짝이면 스택 맨 끝 요소 제거
                if stack[-1] == "[" and queue[j] == "]":
                    stack.pop()
                elif stack[-1] == "(" and queue[j] == ")":
                    stack.pop()
                elif stack[-1] == "{" and queue[j] == "}":
                    stack.pop()
                # 그렇지 않다면 현재 괄호 저장
                else:
                    stack.append(queue[j])
        
        if len(stack) == 0: # 모든 괄호를 돌았을 때, 스택이 비었다면 완벽한 괄호
            answer += 1
        
    return answer