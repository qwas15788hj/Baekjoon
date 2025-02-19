def solution(schedules, timelogs, startday):
    answer = 0
    
    startday -= 1
    for i in range(len(schedules)):
        schedules[i] += 10
        if (schedules[i]%100) >= 60:
            schedules[i] += 40
    
    for i in range(len(schedules)):
        flag = True
        for j in range(len(timelogs[i])):
            day = (startday+j)%7
            if day != 5 and day != 6:
                if timelogs[i][j] > schedules[i]:
                    flag = False
                    break
            if not flag:
                break
        
        if flag:
            answer += 1
    
    return answer