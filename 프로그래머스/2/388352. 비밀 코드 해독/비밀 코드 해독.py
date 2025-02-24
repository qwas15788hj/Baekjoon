from itertools import combinations

def solution(n, q, ans):
    answer = 0
    arr = [i for i in range(1, n+1)]
    comb = list(combinations(arr, 5))
    
    for com in comb:
        flag = True
        for i in range(len(q)):
            count = 0
            for j in range(len(q[i])):
                if q[i][j] in com:
                    count += 1
            if count != ans[i]:
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer