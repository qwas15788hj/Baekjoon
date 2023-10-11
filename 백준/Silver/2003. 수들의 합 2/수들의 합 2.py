n, m = map(int, input().split()) # n, m 입력
arr = list(map(int, input().split())) # 숫자 입력
store = [] # 숫자 저장할 배열
num, answer = 0, 0 # 현재 수, 경우의 수

for i in range(n): # 배열 돌면서
    store.append(arr[i]) # 현재 원소 store에 저장
    num += arr[i] # 현재 원소 num에 더하기

    while num > m: # 현재 수가 m보다 크면
        num -= store.pop(0) # 가장 앞 수 빼기

    # num이 m과 같다면 answer 증가
    if num == m:
        answer += 1

print(answer)