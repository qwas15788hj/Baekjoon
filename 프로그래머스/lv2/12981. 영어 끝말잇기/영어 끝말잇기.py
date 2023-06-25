def solution(n, words):
    answer = [0, 0]
    arr = [words[0]] # 현재까지 나온 단어들 저장하는 배열
    word = words[0] # 이전 단어 저장할 word 변수, 초기 words[0]
    
    for i in range(1, len(words)): # 인덱스 1부터 진행
        # 이전 단어 끝과 현재 부른 단어의 첫번째가 다르거나 현재 부른 단어가 배열에 있다면 실패
        if word[-1] != words[i][0] or words[i] in arr:
            # 부른 사람 구하기
            if (i+1) % n == 0: # 인덱스 % 사람 수가 0이면
                answer[0] = n # 마지막 사람
            else: # 0이 아니면
                answer[0] = (i+1) % n # 인덱스 % 사람 수로 몇번째 사람인지 구하기
            answer[1] = i//n + 1 # 몇번 돌았는지 구하기 (인덱스//사람수 + 1)번
            break # 멈추기
        else: # 끝말잇기 성공했다면
            arr.append(words[i]) # 배열에 저장
            word = words[i] # 이전 단어로 저장
    
    return answer