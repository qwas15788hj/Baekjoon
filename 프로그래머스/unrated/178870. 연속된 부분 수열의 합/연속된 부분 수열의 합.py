from collections import deque

def solution(sequence, k):
    answer = []
    queue = deque() # 원소 저장할 덱
    num = 0 # 원소 총합 저장
    
    for i in range(len(sequence)): # 원소 돌면서
        if num < k: # 현재 큐에 있는 원소 총합이 k 보다 작으면
            queue.append(i) # 큐에 인덱스 저장
            num += sequence[i] # 총합 증가
        else: # 총합이 k 보다 크거나 같으면
            while True: # 무한 반복
                if num > k: # 총합이 k 보다 크면
                    num -= sequence[queue.popleft()] # 큐 맨 앞 요소 빼면서 총합에서 빼주기
                elif num == k: # 총합이 k랑 같다면
                    answer.append([queue[0], queue[-1]]) # answer에 [시작 인덱스, 끝 인덱스] 저장
                    num -= sequence[queue.popleft()] # 큐 맨 앞 요소 빼면서 총합에서 빼주기
                else: # 총합이 k보다 작다면 멈춤
                    break
            queue.append(i) # while 문 종료시 큐에 현재 인덱스 번호 저장 후
            num += sequence[i] # 총합에서 인덱스에 해당하는 값 저장
    
    # for문 이후 큐에 남은 원소 처리
    while queue: # 큐가 빌때까지
        if num == k: # 총합이 k와 같다면
            answer.append([queue[0], queue[-1]]) # answer에 인덱스 저장
        elif num < k: # 총합이 k보다 작으면 멈춤
            break
        num -= sequence[queue.popleft()] # 큐의 맨 앞 요소 계속 빼면서 진행
    
    # 끝 인덱스 - 시작 인덱스 차이 오름차순, 시작 인덱스 오름차순으로 정렬
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    
    return answer[0]