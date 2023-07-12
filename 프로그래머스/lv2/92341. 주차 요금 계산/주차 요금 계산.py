def solution(fees, records):
    answer = []
    
    total_dic = dict() # 차량별 총 시간 딕셔너리
    in_time_dic = dict() # 차량별 입출 시간 딕셔너리

    for record in records: # records 반복
        rec = record.split(" ") # record를 띄어쓰기 기준으로 나누기
        if rec[2] == "IN": # 입차이면
            if rec[1] not in total_dic: # 해당 차량이 total 딕셔너리에 없다면 처음 들어온 차량임으로 등록
                total_dic[rec[1]] = 0 # 등록
            time = int(rec[0][:2]) * 60 + int(rec[0][3:5]) # 입출 시간 구하기 / 시간*60+분
            in_time_dic[rec[1]] = time # 입출 딕셔너리에 해당 차량 입출 시간 등록
        else: # 출차면
            time = int(rec[0][:2]) * 60 + int(rec[0][3:5]) # 출차 시간 구하기 / 시간*60+분
            total_dic[rec[1]] += time - in_time_dic[rec[1]] # 현재 차량의 총 시간에 주차 시간 더하기
            in_time_dic[rec[1]] = -1 # 현재 차량이 출차했으므로 입차 시간 -1으로 갱신
    
    # 입차하고 출차안한 차량들 계산
    for key, value in in_time_dic.items(): # 딕셔너리 key, value로 반복
        if value != -1: # 입차 시간이 -1이 아니면
            time = 23 * 60 + 59 # 23:59분 시간
            total_dic[key] += time - value # 해당 차량의 총 시간에 더하기
    
    car_list = list(total_dic.items()) # 차량별 총 시간 딕셔너리를 리스트로 변환
    car_list.sort(key=lambda x:x[0]) # 차량 번호로 오름차순
    for car in car_list: # 리스트 돌면서
        if car[1] <= fees[0]: # 기본 시간보다 작거나 같으면
            answer.append(fees[1]) # 기본 요금만 계산
        else: # 기본 시간보다 크면
            add_time = (car[1] - fees[0]) // fees[2] # 추가시간 요금구하기,(총시간-기본 시간)//단위시간
            if (car[1] - fees[0]) % fees[2] != 0: # 나누어 떨어지지 않는다면 남은 시간 한 번더 계산
                add_time += 1 # 추가 + 1
            money = fees[1] + add_time * fees[3] # 총 금액 = 기본요금 + 추가 시간 * 추가 금액
            answer.append(money)
            
    return answer