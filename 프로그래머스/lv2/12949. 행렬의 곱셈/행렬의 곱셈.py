def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)): # 0 1 2
        result = []
        for j in range(len(arr2[0])): # 0 1 
            num = 0
            for z in range(len(arr1[0])): # 0 1
                num += arr1[i][z] * arr2[z][j]
            result.append(num)
        answer.append(result)
        
    return answer