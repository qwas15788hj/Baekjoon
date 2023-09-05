import heapq

def solution(n, k, enemy):
    answer = len(enemy) # 초기 값은 모든 라운드를 막을 수 있다는 가정
    
    heap = [] # 우선순위 큐 생성
    flag = False
    
    for i in range(len(enemy)): # 라운드 돌면서
        n -= enemy[i] # n을 일단 현재 라운드 적 수 만큼 뺀 후
        heapq.heappush(heap, [-enemy[i], enemy[i]]) # 현재 적 수 우선순위 큐에 저장
        
        if n < 0: # 현재 n이 0보다 작고
            if k == 0: # 무적권이 없다면 해당 라운드에서 종료
                answer = i
                return answer
            else: # 무적권이 있다면
                n += heapq.heappop(heap)[1] # 적 수가 제일 적었던 라운드를 무적권을 사용해서 막기
                k -= 1
    
    return answer