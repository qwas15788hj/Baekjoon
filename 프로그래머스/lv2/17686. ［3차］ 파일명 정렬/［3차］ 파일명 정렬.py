def solution(files):
    answer = [0] * len(files)
    
    arr = []
    for i in range(len(files)): # 파일들 반복
        head = "" # 헤더
        number = "" # 숫자 부분
        tail = "" # 마지막 부분
        flag = 0 # 현재 위치 체크
        for j in range(len(files[i])): # 현재 파일 반복
            if flag == 0: # 현재 체크가 헤더 위치면
                if files[i][j].isdigit(): # 요소가 숫자면
                    number += files[i][j] # 숫자에 추가
                    flag = 1 # 숫자로 체크 변경
                else: # 숫자가 아니면
                    head += files[i][j].lower() # 소문자로 변경 후 헤더에 추가
            elif flag == 1: # 체크가 숫자면
                if files[i][j].isdigit() and len(number) < 5: # 요소가 숫자이며, 길이가 5 미만이면
                    number += files[i][j] # 숫자에 추가
                else: # 요소가 숫자가 아니거나 5 이상이면
                    tail += files[i][j].lower() # 소문자로 변경 후 꼬리에 추가
                    flag = 2 # 체크 꼬리로 변경
            else: # 체크가 꼬리면
                tail += files[i][j].lower() # 소문자로 변경 후 꼬리에 추가
                
        arr.append([head, int(number), tail, i]) # 배열에 [헤더, 숫자, 꼬리, 인덱스] 순으로 저장
    
    arr.sort(key=lambda x:(x[0], x[1], x[3])) # 헤더, 숫자, 인덱스 순으로 정렬
    
    for i in range(len(arr)): # 구한 배열 돌면서
        answer[i] = files[arr[i][3]] # 현재 배열의 인덱스 번호에 해당하는 파일을 정답에 갱신
    
    return answer