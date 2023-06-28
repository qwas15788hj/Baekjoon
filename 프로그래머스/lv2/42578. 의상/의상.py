def solution(clothes):
    answer = 1
    dic = dict()
    
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 1
    
    for i in dic.values():
        answer *= i + 1
    
    return answer - 1