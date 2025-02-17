def solution(diffs, times, limit):
    answer = 1e9
    
    start = 1
    end = max(diffs)
    while start <= end:
        mid = (start + end)//2
        count = times[0]
        for i in range(1, len(diffs)):
            if mid >= diffs[i]:
                count += times[i]
            else:
                count += (times[i-1] + times[i])*(diffs[i]-mid) + times[i]
        
        if count <= limit:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    
    return answer