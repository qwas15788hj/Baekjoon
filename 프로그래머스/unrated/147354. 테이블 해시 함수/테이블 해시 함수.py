def solution(data, col, row_begin, row_end):
    answer = 0 # 현재 XOR한 값, 초기 값은 0으로
    
    # col-1번째 인덱스 기준으로 오름차순, 같다면 첫 번째 인덱스 기준 내림차순으로 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin - 1, row_end): # row_begin - 1 ~ row_end - 1 까지
        num = 0 # 현재 인덱스 행 mod한 값 모두 더한 값
        for j in data[i]: # 해당 인덱스 행 요소 반복
            num += j % (i+1) # 해당 인덱스 행 요소마다 (행 번호+1)로 나눈 값 answer에 더하기
        answer ^= num # 현재 인덱스 행 mod한 모두 더한 값과 XOR 연산
    
    return answer