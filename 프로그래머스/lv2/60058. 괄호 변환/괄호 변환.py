# 2단계 u, v 나누는 함수
def divide(p):
    left = 0 # ( 개수
    right = 0 # ) 개수
    
    for i in range(len(p)): # p 원소 돌면서
        if p[i] == "(": # ( 면 left 증가
            left += 1
        else: # ) 면 right 증가
            right += 1
        
        if left == right: # left와 right 수가 같은 균형잡힌 괄호 문자열이면
            return p[:i + 1], p[i + 1:] # u는 균형잡힌 괄호 문자열, v는 이후 문자열로 return

# 올바른 괄호 문자열인지 판단하는 함수
def check(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True

# 메인 함수
def solution(p):
    answer = ''
    
    # 1단계
    if len(p) == 0:
        return ""
    
    # 2단계
    u, v = divide(p)
    
    # 3단계
    if check(u):
        # 3-1단계
        return u + solution(v) # u와 메인을 v로 돌린 값 return
    # 4단계
    else:
        answer += "(" # 4-1
        answer += solution(v) # 4-2
        answer += ")" # 4-3
        for i in u[1:len(u) - 1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        
    return answer