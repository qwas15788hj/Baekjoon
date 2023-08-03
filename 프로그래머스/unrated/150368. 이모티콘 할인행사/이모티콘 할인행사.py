from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    sales = [10, 20, 30, 40]
    
    for sale in list(product(sales, repeat = len(emoticons))): # 모든 세일의 종류
        emo = [] # 세일된 이모티콘 값
        plus = 0 # 플러스 가입한 유저 수
        money = 0 # 유저가 사용한 금액
        for i in range(len(sale)): # 세일된 이모티콘 값 구하기
            emo.append(emoticons[i] - (emoticons[i] * sale[i] // 100))
        
        for u in users: # 유저 마다
            u_m = 0 # 유저가 사용한 금액
            for j in range(len(sale)): # 이모티콘 하나씩 확인
                if u[0] <= sale[j]: # 유저가 원하는 세일보다 현재 세일을 더 많이하거나 같으면
                    u_m += emo[j] # 해당 이모티콘 구매
            if u_m >= u[1]: # 유저가 사용한 금액이 자신이 원하는 금액보다 크거나 같으면
                plus += 1 # 플러스 가입
            else: # 원하는 금액보다 적게 사용하면
                money += u_m # 금액만 증가
                
        if plus > answer[0]: # 플러스 가입 인원이 기존 보다 많으면
            answer[0], answer[1] = plus, money # 갱신
        elif plus == answer[0]: # 플러스 가입 인원이 기존과 같으면
            answer[1] = max(answer[1], money) # 가격만 비교하여 갱신
            
    return answer