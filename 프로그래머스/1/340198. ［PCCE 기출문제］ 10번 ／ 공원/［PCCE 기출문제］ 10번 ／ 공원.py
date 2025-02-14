def solution(mats, park):
    answer = -1
    n = len(park)
    m = len(park[0])
    mats.sort(reverse=True)
    
    arr = []
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                arr.append([i, j])
    
    for mat in mats:
        for x, y in arr:
            flag = True
            for i in range(x, x+mat):
                for j in range(y, y+mat):
                    if i < 0 or i >= n or j < 0 or j >= m:
                        flag = False
                        break
                    if park[i][j] != "-1":
                        flag = False
                        break
            
            if flag:
                answer = max(answer, mat)
        
        if answer == mats[0]:
            break
    
    return answer