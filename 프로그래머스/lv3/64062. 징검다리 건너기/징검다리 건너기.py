def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left+right)//2
        count = 0
        for stone in stones: #돌마다
            if stone-mid <= 0: #돌-건넌수 = 음수면
                count += 1 #못건너는 돌
            else:
                count = 0 #건너감
            
            if count >= k: #이미 못건넘
                break
        
        if count >= k: #못건너면 건너는 수 줄이기
            right = mid-1
        else: #건널수 있으니 저장
            left = mid+1
            answer = left
            
    return answer