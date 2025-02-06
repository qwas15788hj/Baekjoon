def solution(ingredient):
    answer = 0
    
    arr = []
    n = len(ingredient)
    for i in range(n):
        if len(arr) >= 3 and ingredient[i] == 1 and arr[-1] == 3 and arr[-2] == 2 and arr[-3] == 1:
            for _ in range(3):
                arr.pop()
            answer += 1
        else:
            arr.append(ingredient[i])
    
    return answer