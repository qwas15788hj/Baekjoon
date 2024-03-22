def solution(friends, gifts):
    answer = []
    arr = [[0] * len(friends) for _ in range(len(friends))]
    score = dict()
    for friend in friends:
        score[friend] = 0
    
    for i in range(len(gifts)):
        a = gifts[i].split(" ")[0]
        b = gifts[i].split(" ")[1]
        a_idx = friends.index(a)
        b_idx = friends.index(b)
        
        arr[a_idx][b_idx] += 1
        score[a] += 1
        score[b] -= 1
    
    
    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i != j:
                if arr[i][j] > arr[j][i]:
                    count += 1
                elif arr[i][j] == arr[j][i]:
                    if score[friends[i]] > score[friends[j]]:
                        count += 1
        
        answer.append(count)
    
    return max(answer)