def solution(want, number, discount):
    answer = 0
    
    dic = dict() # 물품과 수량을 의미하는 딕셔너리
    count = sum(number) # 총 필요한 물품 갯수
    for i in range(count): # 갯수 반복
        if discount[i] in dic: # 해당 물품이 딕셔너리에 있다면
            dic[discount[i]] += 1 # + 1
        else: # 없다면
            dic[discount[i]] = 1 # 추가
    
    flag = True
    for i in range(len(want)): # 원하는 물품을 반복하며
        # 원하는 물품이 딕셔너리에 없거나, 딕셔너리에 있지만 필요 물품 수보다 작으면 회원가입 안함
        if want[i] not in dic or dic[want[i]] < number[i]:
            flag = False
            break
    if flag: # 살 수 있다면
        answer += 1 # 회원가입 + 1
    
    for i in range(len(discount) - count): # 물품 수 - 필요 수 만큼 반복
        dic[discount[i]] -= 1 # 맨 앞 물품 빼고
        if discount[i + count] in dic: # 추가될 물품 추가 dic에 있다면
            dic[discount[i + count]] += 1 # + 1
        else: # 없다면
            dic[discount[i + count]] = 1 # 추가
        
        # 위의 코드 반복
        flag = True
        for j in range(len(want)):
            if want[j] not in dic or dic[want[j]] < number[j]:
                flag = False
                break
        
        if flag:
            answer += 1
        
    return answer