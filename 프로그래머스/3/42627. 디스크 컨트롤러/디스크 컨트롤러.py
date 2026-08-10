from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    
    n = len(jobs)
    arr = []
    for i in range(n):
        jobs[i] = jobs[i] + [i]
    jobs.sort(key=lambda x:x[0])
    
    cnt = 0
    idx = 0
    time = jobs[0][0]
    while cnt != n:
        while idx < n and jobs[idx][0] <= time:
            heappush(arr, [jobs[idx][1], jobs[idx][0], jobs[idx][2]])
            idx += 1
        
        if len(arr) == 0 and idx < n:
            time = jobs[idx][0]
            continue
        else:
            t, s, i = heappop(arr)
            answer += (time + t) - s
            time += t
            cnt += 1
    
    return answer//n