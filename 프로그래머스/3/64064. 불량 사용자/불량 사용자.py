from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    
    for check in list(permutations(user_id, len(banned_id))):
        flag = True
        check = list(check)
        
        for i in range(len(check)):
            if len(check[i]) != len(banned_id[i]):
                flag = False
                break
                
            for j in range(len(check[i])):
                if banned_id[i][j] != "*" and banned_id[i][j] != check[i][j]:
                    flag = False
                    break
        
        if flag:
            check.sort()
            if check not in answer:
                answer.append(check)
    
    return len(answer)