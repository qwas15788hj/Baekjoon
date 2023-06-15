def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0 or stack[-1] == ")":
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False