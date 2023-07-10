def solution(phone_book):
    answer = True
    
    phone_book.sort(key = lambda x:len(x)) # 길이 순으로 오름차순
    dic = dict() # 번호 저장할 딕셔너리
    for i in range(len(phone_book)): # 정렬한 전화번호 돌면서
        size = len(phone_book[i]) # 현재 전화번호의 길이
        for j in range(1, size + 1): # 1 ~ 현재 전화번호의 길이까지 돌면서
            if phone_book[i][:j] in dic: # 현재 전화번호의 앞쪽 길이가 딕셔너리에 존재한다면
                answer = False # 접두어
                break
        if answer == False:
            break
        else: # 현재 전화번호의 앞쪽 길이가 딕셔너리에 존재하지 않다면
            dic[phone_book[i]] = 1 # 딕셔너리에 추가
    
    return answer