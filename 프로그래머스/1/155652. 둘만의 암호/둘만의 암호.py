def solution(s, skip, index):
    answer = ''
    
    arr = []
    for i in range(ord("a"), ord("z")+1):
        if chr(i) not in skip:
            arr.append(chr(i))
    
    for i in range(len(s)):
        idx = arr.index(s[i])
        answer += arr[(idx+index)%len(arr)]
    
    return answer