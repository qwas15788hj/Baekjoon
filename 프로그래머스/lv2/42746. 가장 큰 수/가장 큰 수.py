def solution(numbers):
    answer = ""
    
    numbers.sort(key=lambda x:str(x)*4) # numbers 원소가 최대 1000까지 4자리임으로 4자리 수 맞춰서 정렬
    for i in range(len(numbers) - 1, -1, -1): # 끝번호부터 큰 수대로 answer에 더하기
        answer += str(numbers[i])
    
    if int(answer) == 0: # answer 원소가 0만 있으면 
        answer = "0" # 0으로 바꿔주기 (예외처리)
        
    return answer