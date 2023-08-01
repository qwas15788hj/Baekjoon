def solution(order):
    answer = 0 # 실은 갯수
    arr = [] # 보조 컨테이너
    idx = 0 # 현재 배달해야하는 물품 인덱스 번호
    
    for i in range(len(order)): # 물품 돌면서
        if order[idx] == i + 1: # 현재 배달해야하는 물품의 인덱스가 현재 박스 번호와 같다면
            idx += 1 # 인덱스 증가
            answer += 1 # 개수 증가
        else: # 번호가 다르다면
            arr.append(i + 1) # 보조 컨테이너에 올리기
        
        while arr: # 보조 컨테이너 돌면서
            # 보조 컨테이너에 물건이 없거나 현재 물품과 다르다면 멈춤
            if len(arr) == 0 or arr[-1] != order[idx]:
                break
            arr.pop() # 같다면 보조 컨테이너에서 꺼내고
            idx += 1 # 인덱스 즞ㅇ가
            answer += 1 # 개수 증가
            
    return answer