def solution(players, callings):
    n = len(players)
    m = len(callings)
    arr = [""] * (n+1)
    dic = dict()
    
    for i in range(n):
        arr[i+1] = players[i]
        dic[players[i]] = i+1
    
    for i in range(m):
        idx = dic[callings[i]]
        dic[arr[idx-1]] = idx
        dic[arr[idx]] = idx-1
        arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
    
    answer = [""] * n
    for key, value in dic.items():
        answer[value-1] = key
    
    return answer