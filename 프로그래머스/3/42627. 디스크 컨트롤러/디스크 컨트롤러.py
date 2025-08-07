from heapq import heappush, heappop

def solution(jobs):
    n = len(jobs)
    answer = [0] * n
    
    for i in range(n):
        jobs[i].append(i)
    arr = []
    time = 0
    idx = 0
    jobs.sort(key=lambda x:x[0])
    while True:
        if 0 not in answer:
            break

        while idx != n:
            if jobs[idx][0] <= time:
                heappush(arr, [jobs[idx][1], jobs[idx][0], jobs[idx][2]])
                idx += 1
            else:
                break
        
        if len(arr):
            job = heappop(arr)
            time += job[0]
            answer[job[2]] = time-job[1]
        elif len(arr) == 0 and idx <= n:
            time = jobs[idx][0]
            
    return sum(answer)//n