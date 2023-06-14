def solution(s):
    subArr = list(map(str, s.split(" ")))
    arr = [0]*len(subArr)
    for i in range(len(arr)):
        arr[i] = int(subArr[i])
    
    answer = str(min(arr)) + " " + str(max(arr))
    return answer