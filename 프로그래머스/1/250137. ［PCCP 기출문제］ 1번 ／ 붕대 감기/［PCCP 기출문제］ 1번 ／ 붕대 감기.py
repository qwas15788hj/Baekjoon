def solution(bandage, health, attacks):
    answer = 0
    max_h = health
    flag = True
    
    count, idx, time = 0, 0, 0
    for i in range(1, attacks[-1][0]+1):
        time += 1
        if attacks[idx][0] == time:
            health -= attacks[idx][1]
            count = 0
            idx += 1
            if health <= 0:
                flag = False
                break
        else:
            count += 1
            health += bandage[1]
            if count == bandage[0]:
                health += bandage[2]
                count = 0
            
            health = min(health, max_h)
    
    if flag:
        return health
    else:
        return -1