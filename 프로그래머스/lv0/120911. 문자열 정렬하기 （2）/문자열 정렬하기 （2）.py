def solution(my_string):
    answer = ''
    
    arr = []
    a = my_string.lower()
    for i in a:
        arr.append(i)
    arr.sort()
    
    for i in arr:
        answer += i
    
    return answer