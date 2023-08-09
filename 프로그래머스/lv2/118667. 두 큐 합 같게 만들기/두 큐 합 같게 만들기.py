from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1) # 첫번째 큐
    queue2 = deque(queue2) # 두번째 큐
    count1 = 0 # 첫번째 큐 변경 횟수
    count2 = 0 # 두번째 큐 변경 횟수
    size = len(queue1) + len(queue2) # 총 사이즈
    num1 = sum(queue1) # 첫번째 큐 합
    num2 = sum(queue2) # 두번째 큐 합
    total = num1 + num2 # 두 큐의 총합
    flag = False # 성공 or 실패 여부
    
    while True:
        # 두 큐의 총합이 홀수면 실패
        if total % 2 != 0:
            break
        # 첫번째 큐, 두번째 큐 모두 총합의 반이랑 같으면 성공
        if num1 == total//2 and num2 == total//2:
            flag = True
            break
        # 첫번째 큐의 합이 더 크면
        if num1 > num2:
            num1 -= queue1[0] # 첫번째 큐 합에서 맨 앞 요소만큼 빼고
            queue2.append(queue1.popleft()) # 두번째 큐에 첫번째 큐 맨 앞 요소 저장
            num2 += queue2[-1] # 두번째 큐에 들어온 마지막 원소 더하기
            count1 += 1 # 첫번째 큐 카운트 증가
        else: # 두번째 큐의 합이 더 크면
            num2 -= queue2[0] # 두번째 큐 합에서 맨 앞 요소만큼 빼고
            queue1.append(queue2.popleft()) # 첫번째 큐에 두번째 큐 맨 앞 요소 저장
            num1 += queue1[-1] # 첫번째 큐에 들어온 마지막 원소 더하기
            count2 += 1 # 첫번째 큐 카운트 증가
        
        # 한쪽이 모든 원소를 가져가면 실패
        if len(queue1) == size or len(queue2) == size:
            break
        # 한쪽의 이동횟수가 요소의 모든 개수일 경우 모든 경우를 다한 경우임으로 실패처리 후 종료
        if count1 == size or count2 == size:
            break
        
        answer += 1 # 모든 처리를 완료 후 작업 횟수 증가
        
    # 정답 처리 flag가 False면 실패임으로
    if flag == False:
        answer = -1
    
    return answer