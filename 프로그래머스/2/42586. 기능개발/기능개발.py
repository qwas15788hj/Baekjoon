def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    arr = [0] * n
    for i in range(n):
        day = (100-progresses[i]) // speeds[i]
        if (progresses[i] + speeds[i] * day) != 100:
            day += 1
        arr[i] = day
    
    now = arr[0]
    count = 0
    for i in range(n):
        if arr[i] > now:
            answer.append(count)
            now = arr[i]
            count = 1
        else:
            count += 1
    
    if count != 0:
        answer.append(count)
        
    return answer