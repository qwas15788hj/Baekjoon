from itertools import product
def solution(cost, hint):
    answer = 1e9
    c, h = len(cost), len(hint)
    
    check = ['o', 'x']
    a = 0
    for prod in list(product(check, repeat=h)):
        buy = [0] * c
        result = cost[0][0]
        for i in range(len(prod)):
            if prod[i] == 'o':
                result += hint[i][0]
                for j in range(1, len(hint[i])):
                    buy[hint[i][j]-1] += 1
        
        for i in range(1, c):
            idx = min(len(cost[i])-1, buy[i])
            result += cost[i][idx]
        
        answer = min(answer, result)
        
        
    return answer