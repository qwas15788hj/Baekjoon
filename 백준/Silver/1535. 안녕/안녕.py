n = int(input()) # n 입력
hp = [0] + list(map(int, input().split())) # 잃는 체력 입력
happy = [0] + list(map(int, input().split())) # 얻는 기쁨 입력

arr = [[0]*101 for _ in range(n+1)] # 1~100체력 n+1줄 배열 생성
for i in range(1, n+1): # n명 반복
    for j in range(1, 101): # 체력 1~100 반복
        if hp[i] <= j: # 잃는 체력이 현재 체력보다 작거나 같으면
            # 현재 만나 얻는 기쁨과 현재 안만나고 이전에 얻는 기쁨 비교하여 큰 값으로
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-hp[i]] + happy[i])
        else:
            arr[i][j] = arr[i-1][j]

print(max(arr[-1][:100])) # 100번째 인덱스는 체력이 0이므로 99까지