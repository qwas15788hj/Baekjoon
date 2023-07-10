def solution(n, k):
    answer = 0
    num_list = []
    
    num = ''
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    
    result = ''
    for i in num[::-1]:
        if i != '0':
            result += i
        else:
            if result == '':
                pass
            else:
                num_list.append(int(result))
                result = ''
    
    if result != '':
        num_list.append(int(result))
    
    for i in num_list:
        if i == 1:
            pass
        else:
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
            else:
                answer += 1
    
    return answer