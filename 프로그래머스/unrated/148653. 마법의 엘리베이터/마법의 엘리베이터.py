def solution(storey):
    answer = 0
    
    # 현재 자리 수가 6이상이면 10까지 올라가고 내려가기
    # 현재 자리 수가 4이하면 그대로 내려가기
    # 현재 자리 수가 5면 다음 자리 수 확인하여
    # 다음 자리수 가 5이상이면 현재 자리 수 10으로 올라가고
    # 다음 자리 수가 4이하면 현재 자리수 내리기
    while storey:
        now = storey % 10 # 현재 자리 수 값
        
        # 현재 자리 수 6이상
        if now > 5:
            answer += (10 - now) # 10 - 현재 값ㅂ
            storey += 10 # 10층 올라가기
        # 현재 자리 수 4이하
        elif now < 5:
            answer += now # 현재 값 그대로 내려가기
        # 현재 값 5
        else:
            if (storey // 10) % 10 > 4: # 다음 자리 수가 5이상이면
                storey += 10 # 10층으로 이동
            answer += now # 현재 층 값 더해주기
        
        storey //= 10 # 층 수 다음 자리 수로
        
    return answer