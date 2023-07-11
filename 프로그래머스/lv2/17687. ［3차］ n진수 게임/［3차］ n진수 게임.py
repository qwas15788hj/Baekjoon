def solution(n, t, m, p):
    answer = ""
    num = 1 # 시작 숫자
    count = 2
    
    while True:
        now = change(num, n)
        for i in range(len(now)):
            if count == p:
                answer += now[i]
            count += 1
            if count > m:
                count = 1
                
        num += 1
        if len(answer) >= t:
            break
    
    if p == 1:
        answer = "0" + answer
    
    return answer[:t]

def change(num, n):
    s = ""
    while num > 0:
        num, mod = divmod(num, n)
        s += alpha(mod)
    return s[::-1]

def alpha(mod):
    alpha = ""
    if mod == 10:
        alpha = "A"
    elif mod == 11:
        alpha = "B"
    elif mod == 12:
        alpha = "C"
    elif mod == 13:
        alpha = "D"
    elif mod == 14:
        alpha = "E"
    elif mod == 15:
        alpha = "F"
    else:
        alpha = str(mod)
    return alpha