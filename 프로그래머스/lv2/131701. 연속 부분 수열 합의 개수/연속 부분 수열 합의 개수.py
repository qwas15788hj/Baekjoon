from collections import deque

def solution(elements):
    answer = set() # 중복 허용 안하는 set 집합으로 선언
    queue = deque(elements) # elements를 큐로 선언
    
    for i in range(1, len(elements)): # i를 길이로 생각 후 선언 1 ~ 길이-1 까지 => 합을 위해서
        num = sum(list(queue)[:i]) # 맨 처음 i만큼 더한 값
        for j in range(len(elements)): # 큐를 원래로 되돌리려면 길이만큼 반복
            now = queue.popleft()
            queue.append(now) # 큐 맨 끝에 큐 맨 앞의 요소를 삽입
            num = num - now + queue[i-1]
            answer.add(num)
            # answer.add(sum(list(queue)[:i])) # 큐를 list로 변환 후 i만큼 합을 answer에 저장
    
    answer.add(sum(list(queue))) # 총 합을 answer에 저장
    
    return len(answer)