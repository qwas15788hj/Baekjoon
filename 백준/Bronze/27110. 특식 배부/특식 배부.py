n = int(input()) # n 입력
arr = list(map(int, input().split())) # 선호 치킨 입력
answer = 0 # 최대 인원수
for i in range(len(arr)): # 선호 치킨 돌면서
    answer += min(arr[i], n) # 선호도와 치킨 개수 중 작은 값 answer 에 더하기

print(answer)