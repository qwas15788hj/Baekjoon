def solution(today, terms, privacies):
    answer = []
    dic = dict()
    for i in range(len(terms)):
        alpha, time = terms[i].split(" ")
        dic[alpha] = int(time)*28
    
    now = int(today[:4])*12*28 + int(today[5:7])*28 + int(today[8:])
    for i in range(len(privacies)):
        time, alpha = privacies[i].split(" ")
        prev = int(time[:4])*12*28 + int(time[5:7])*28 + int(time[8:])
        if dic[alpha] <= now - prev:
            answer.append(i+1) 
            
    return answer