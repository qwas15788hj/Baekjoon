def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    
    while left <= right:
        mid = (left + right)//2
        
        count = 0
        for stone in stones:
            if stone - mid < 0:
                count += 1
            else:
                count = 0
            
            if count >= k:
                break
        
        if count < k:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
            
    return answer