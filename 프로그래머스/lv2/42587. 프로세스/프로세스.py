from collections import deque

def solution(priorities, location):
    answer = 0
    
    dic = dict() # 우선순위 저장할 딕셔너리
    for i in range(len(priorities)): # 길이만큼 반복하며 딕셔너리에 인덱스 : 우선순위로 저장
        dic[i] = priorities[i]
    
    queue = deque() # 큐 선언
    for i in range(len(priorities)): # 큐에 인덱스 저장
        queue.append(i)
        
    while queue: # 큐 돌면서
        now = queue[0] # 큐의 맨 앞 확인
        flag = True # 체크 변수
        for i in range(1, len(queue)): # 큐의 원소 1 ~ 끝까지
            if dic[queue[i]] > dic[now]: # 큐의 원소의 우선순위가 현재 확인하는 우선순위보다 크면
                flag = False # 체크 변환 후 끝
                break
        
        if flag: # 현재 맨 앞이 우선순위 제일 크면
            queue.popleft() # 빼고
            answer += 1 # + 1
        else: # 현재 맨 앞보다 우선순위 높은 것이 있다면
            queue.append(queue.popleft()) # 큐에 다시 삽입
        
        if flag and now == location: # 현재 맨 앞이 우선순위 제일 크고 타겟이면
            break # 멈춤
        
    return answer