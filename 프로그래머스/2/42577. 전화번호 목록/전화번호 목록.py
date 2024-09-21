def solution(phone_book):
    answer = True
    
    n = len(phone_book)
    phone_book.sort(key=lambda x:len(x))
    dic = dict()
    for i in range(n):
        size = len(phone_book[i])
        for j in range(1, size+1):
            if phone_book[i][:j] in dic:
                answer = False
                break
        else:
            dic[phone_book[i]] = 1
    
    return answer