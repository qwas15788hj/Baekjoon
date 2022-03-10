def solution(numbers, target):
    answer = 0
    result = [0]
    
    for num in numbers:
        num_list = []
        for res in result:
            num_list.append(res + num)
            num_list.append(res - num)
        result = num_list
    
    for r in result:
        if r == target:
            answer += 1
    
    return answer