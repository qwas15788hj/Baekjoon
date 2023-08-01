def solution(numbers):
    answer = []
    
    for number in numbers: # 배열 돌면서
        if number % 2 == 0: # 원소가 짝수면 맨 뒤 비트만 바뀌면 됨으로
            answer.append(number + 1) # + 1 한 값 answer에 저장
        else: # 원소가 홀수면 맨 뒤에 0이 나오면 해당 인덱스를 1로 변경 후 해당 인덱스 다음 부분을 0으로 변경
            num = "0" + bin(number)[2:] # 7의 경우 111이기에 0을 맨 앞에 추가하여 시작
            idx = 0 # 인덱스 저장
            for i in range(len(num)-1, -1, -1): # 원소 2진수 맨 뒤부터 탐색하면서
                if num[i] == "0": # 0이면 인덱스 저장 후 멈춤
                    idx = i
                    break
                    
            # 인덱스 전까지 그대로 + 1로 변경 + 0으로 변경 + 인덱스 + 2부터 그대로
            num = num[:idx] + "10" + num[idx+2:]
            answer.append(int(num, 2)) # 나온 2진수를 10진수로 변경 후 answer에 저장
            
    return answer