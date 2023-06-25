def solution(s):
    answer = 0
    flag = True
    
    while True:
        stack = []
        count = 0
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop()
                    count += 1
                else:
                    stack.append(s[i])
        
        if count == 0 or len(stack) == 0:
            break
        else:
            s = "".join(stack)
    
    if len(stack) == 0:
        answer = 1
    
    return answer