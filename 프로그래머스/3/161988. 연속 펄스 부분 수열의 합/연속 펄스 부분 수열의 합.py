def solution(sequence):
    answer = 0
    
    n = len(sequence)
    a, b = sequence.copy(), sequence.copy()
    for i in range(n):
        if i%2 == 0:
            a[i] *= -1
        else:
            b[i] *= -1
        
    answer = max(max(a), max(b))
    num = 0
    for i in range(n):
        num += a[i]
        if num < 0:
            num = 0
        answer = max(answer, num)
    
    num = 0
    for i in range(n):
        num += b[i]
        if num < 0:
            num = 0
        answer = max(answer, num)
    
    return answer