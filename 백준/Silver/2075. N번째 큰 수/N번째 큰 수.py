import heapq # 우선순위 큐 사용

n = int(input()) # n 입력
arr = [] # n 개의 큰 수들을 저장할 배열
for i in range(n):
    s = list(map(int, input().split())) # 숫자 배열 입력
    for j in range(n):
        if i == 0: # n 개 줄 중 첫 번째 줄이면 모두 저장
            heapq.heappush(arr, s[j])
        else: # 첫 번째 이후 줄이면
            if s[j] > arr[0]: # 해당 요소가 arr 중 가장 작은 수보다 크면
                heapq.heappop(arr) # 가장 작은 수 빼기
                heapq.heappush(arr, s[j]) # 해당 요소 저장

print(heapq.heappop(arr)) # arr 에서 가장 작은 값 출력