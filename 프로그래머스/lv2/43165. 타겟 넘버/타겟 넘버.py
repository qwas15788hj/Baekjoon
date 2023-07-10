def solution(numbers, target):
    answer = 0
    result = [0] # 첫 시작은 0으로 해야 변화없음
    
    for num in numbers: # numbers 돌면서
        num_list = [] # 저장 리스트 선언
        for res in result: # 현재까지 나온 결과 값들을 돌면서
            num_list.append(res + num) # 현재 결과 값 위치와 현재 num을 더해서 저장
            num_list.append(res - num) # 현재 결과 값 위치와 현재 num을 빼서 저장
        result = num_list # 결과 값을 num_list로 갱신
    
    for res in result: # 마지막으로 나온 결과 리스트들을 돌면서
        if res == target: # 결과 값이 타겟 값과 같다면
            answer += 1 # + 1
    
    return answer