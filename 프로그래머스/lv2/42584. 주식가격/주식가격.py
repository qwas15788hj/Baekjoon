def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1): # 마지막 제외 반복
        for j in range(i+1, len(prices)): # i+1 부터 ~ 끝까지
            if prices[i] <= prices[j]: # 가격이 떨어지지 않으면
                answer[i] += 1 # + 1
            else: # 가격이 떨어지면
                answer[i] += 1 # + 1 하고 종료
                break
            
    return answer