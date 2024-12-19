from collections import deque

t = int(input()) # 테스트케이스 입력
for _ in range(t): # 테스트케이스 반복
    p = input() # 수행할 함수 입력
    n = int(input()) # 배열에 들어있는 수 n 입력
    arr = input() # 배열 입력
    arr = arr.replace("[", "") # 입력받은 배열에 [ => "" 변경
    arr = arr.replace("]", "") # 입력받은 배열에 ] => "" 변경
    arr = arr.replace(",", " ") # 입력받은 배열에 , => " " 변경
    queue = deque(list(map(int, arr.split()))) # 바꾼 배열 띄어쓰기 기준으로 나누어 int형으로 큐에 저장

    if p.count("D") > len(queue): # 버리기 명령어 D가 큐 원소보다 많으면 에러
        print("error") # 에러 출력
    else: # 버리기 명령어가 큐 원소보다 작거나 같으면
        count = 0 # 몇 번 뒤집었는지 카운트
        for i in p: # 명령어 하나씩 확인
            if i=="R": # 명령어가 뒤집기 R이면
                count += 1 # 카운트 증가
            else: # 명령어가 버리기 D이면
                if count%2==0: # 카운트가 짝수면 => 원래 상태 그대로와 같음
                    queue.popleft() # 맨 앞 버리기, 시간복잡도 O(1)
                else: # 카운트가 홀수면 => 뒤집은 상태
                    queue.pop() # 맨 앞 버려야하지만 뒤집은 상태이므로 맨 뒤 버리기, 시간복잡도 O(1)

        if count%2==0: # 카운트가 짝수면 => 원래 상태 그대로
            print('['+','.join(map(str, queue))+']') # 출력 형식 맞춰서 queue 출력
        else: # 카운트가 홀수면 => 뒤집은 상태
            arr = [] # 새로운 배열 생성, queue는 뒤집기 안됨!!
            for i in queue: # 큐 원소
                arr.append(i) # 새로운 배열 arr에 넣어주기
            print('['+','.join(map(str, arr[::-1]))+']') # 출력 형식 맞춰서 뒤집은 arr 출력