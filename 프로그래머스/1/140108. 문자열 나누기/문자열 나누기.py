def solution(s):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    idx = 0
    while True:
        if idx == len(s):
            break
        
        if cnt1 == cnt2:
            now = s[idx]
        
        if now == s[idx]:
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt1 == cnt2:
            answer += 1
            cnt1 = 0
            cnt2 = 0
        
        idx += 1
    
    if cnt1 != 0 or cnt2 != 0:
        answer += 1
        
    return answer