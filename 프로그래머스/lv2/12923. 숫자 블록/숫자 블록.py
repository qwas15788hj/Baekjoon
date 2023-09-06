def solution(begin, end):
    answer = []
    
    # 해당 수의 최소 약수로 나눈 값 찾기
    for i in range(begin, end + 1):
        if i == 1: # 1이면 0 저장
            answer.append(0)
        else: # 1이 아니면
            arr = [1] # 약수 저장할 배열
            k = 0 # 가장 큰 약수를 찾으면 저장할 변수
            # 약수 찾기
            for j in range(2, int(i**0.5) + 1):
                if i%j == 0: # j 가 i 의 약수면
                    arr.append(j) # 배열에 저장
                    if i//j <= 10000000: # 만약 10^7 이하면 i 의 약수 중 가장 큰 값인 i//j 저장
                        k = i//j
                        break
                if k != 0:
                    break
                    
            if k != 0: # k 를 찾았다면 넣고
                answer.append(k)
            else: # k 를 못 찾았다면
                answer.append(arr[-1]) # 배열에 저장된 맨 마지막 값 저장
        
    return answer