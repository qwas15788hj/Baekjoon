def solution(topping):
    answer = 0
    
    a = [0] * 10001 # 철수가 가진 topping 원소
    b = [0] * 10001 # 동생이 가진 topping 원소
    for i in topping: # 초기에는 모두 다 동생이 갖기
        b[i] += 1
    
    a_count = 0 # 형이 가진 토픽 갯수
    b_count = len(set(topping)) # 동생이 가진 토픽 갯수, 초기 모두 가짐
    
    for i in topping: # 토픽 요소 돌면서
        if a[i] == 0: # 형이 현재 토픽이 없다면
            a_count += 1 # 형이 가진 토픽 갯수 + 1 증가
        a[i] += 1 # 형 토픽 요소 + 1
        
        b[i] -= 1 # 동생 토픽 요소 - 1
        if b[i] == 0: # 동생이 형에게 토픽을 줘서 0이 되었으면
            b_count -= 1 # 동생이 가진 토픽 갯수 - 1 감소
        
        if a_count == b_count: # 형이 가진 토픽과 동생이 가진 토픽 수가 같다면
            answer += 1 # 방법 + 1 증가
        
    return answer