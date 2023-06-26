def solution(citations):
    answer = 0
    arr = [0] * 10001 # 최대 10000회
    
    for i in range(len(citations)):
        arr[citations[i]] += 1 # 발표한 논문의 횟수의 요소를 배열에 저장
    
    for i in range(9999, -1, -1): # 맨 끝부터 누적합
        arr[i] += arr[i+1] # 현재 위치의 누적합 = 현재 위치 + 뒤의 위치
    
    for i in range(10000, -1, -1): # 맨 끝부터
        if arr[i] >= i: # 발표한 논문이 h번 이상이면 끝
            answer = i
            break

    return answer