def solution(s):
    answer = ''
    arr = list(map(str, s.split(" ")))
    for i in range(len(arr)):
        word = ""
        for j in range(len(arr[i])):
            if j == 0:
                word += arr[i][j].upper()
            else:
                word += arr[i][j].lower()
        answer += word + " "
    
    return answer[:len(answer)-1]