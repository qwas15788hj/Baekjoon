import math

def solution(r1, r2):
    answer = 0
    
    for i in range(0, r1):
        answer += int(math.sqrt(r2**2 - i**2)) - int(math.sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        answer += int(math.sqrt(r2**2 - i**2))
    
    return answer * 4