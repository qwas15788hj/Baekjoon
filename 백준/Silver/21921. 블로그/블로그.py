n, x = map(int, input().split()) # n, x 입력
arr = list(map(int, input().split())) # 방문자 수 입력
add_arr = [sum(arr[:x])] # 누적합 사용, x일 전까지 누적 방문자수 저장

for i in range(x, len(arr)): # x일 ~ 마지막 날 까지
    # 이전 누적 방문자 수 + 오늘 방문자 수 - (오늘 - x요일 전) 저장
    add_arr.append(add_arr[-1] + arr[i] - arr[i-x])

num = max(add_arr) # 누적 방문자 수 중 가장 많은 방문자 수

if num == 0: # 가장 많은 방문자 수가 0이면
    print("SAD") # "SAD" 출력
else: # 0이 아니면
    print(num) # 방문자 수 출력
    print(add_arr.count(num)) # 가장 많은 방문자 수의 기간 출력