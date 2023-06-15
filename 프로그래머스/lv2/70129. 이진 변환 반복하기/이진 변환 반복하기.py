def solution(s):
    count = 0
    zero = 0
    
    while True:
        if s == "1":
            break
        
        num = 0
        for i in range(len(s)):
            if s[i] == "1":
                num += 1
            else:
                zero += 1
                
        s = bin(num)[2:]
        count += 1
    
    return [count, zero]