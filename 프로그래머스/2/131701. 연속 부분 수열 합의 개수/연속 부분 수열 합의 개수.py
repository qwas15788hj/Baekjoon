def solution(elements):
    answer = set()
    
    elements = [0] + elements
    n = len(elements)
    elements += elements[1:]
    
    # for i in range(len(elements)):
    #     answer.add(elements[i])
    
    # 0 7 9 1 1 4
    # 0     3
    for i in range(n):
        left, right = 0, i
        num = sum(elements[left+1:right])
        while left != n-1:
            num -= elements[left]
            num += elements[right]
            answer.add(num)
            
            left += 1
            right += 1
    
    return len(answer)-1