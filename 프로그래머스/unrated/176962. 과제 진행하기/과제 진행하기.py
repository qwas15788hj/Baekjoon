from collections import deque

def solution(plans):
    answer = []
    stack = [] # 한번은 수행한 과제 넣을 스택 생성
    
    for plan in plans: # 시간을 분으로 모두 변경하여 단위 맞춰주기
        plan[1] = int(plan[1][0] + plan[1][1]) * 60 + int(plan[1][3] + plan[1][4])
        plan[2] = int(plan[2])
        
    plans.sort(key=lambda x:x[1]) # 시작시간으로 오름차순
    
    for i in range(len(plans)): # 과제 돌면서
        if i == len(plans) - 1: # 마지막 과제
            stack.append(plans[i]) # 스택에 넣기
            break
        
        if plans[i][1] + plans[i][2] <= plans[i+1][1]: # 다음 과제 시작 전 현재 과제를 마칠 수 있다면
            answer.append(plans[i][0]) # 현재 과제 마침
            time = plans[i+1][1] - (plans[i][1] + plans[i][2]) # 남은 시간
            while time != 0 and stack: # 남은 시간이 있고, 스택에 과제가 있다면
                if time >= stack[-1][2]: # 최근 진행한 과제가 남은시간보다 작거나 같으면
                    answer.append(stack[-1][0]) # 과제 종료
                    time -= stack[-1][2] # 남은 시간 갱신
                    stack.pop() # 스택에서 빼기
                else: # 남은 시간이 더 작으면
                    stack[-1][2] -= time # 최근 진행한 과제의 남은 시간만 갱신
                    time = 0 # 남은 시간은 0으로
        else: # 다음 과제 시작 전 과제를 못 마치면
            plans[i][2] -= (plans[i+1][1] - plans[i][1]) # 현재 과제 남은 시간 갱신 후
            stack.append(plans[i]) # 스택에 넣기
    
    while stack: # 남은 과제들 순서대로 꺼내기
        answer.append(stack.pop()[0])
    
    return answer