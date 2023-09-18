import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n, k 입력
arr = list(map(int, input().split())) # 온도 입력
add_arr = [] # 누적합 사용할 배열 생성

add_arr.append(sum(arr[:k])) # k일까지 합 누적합에 저장
for i in range(k, n): # k일 ~ 마지막날까지
    add_arr.append(add_arr[-1] + arr[i] - arr[i-k]) # 마지막날 + 오늘 온도 - 가장 오랜된 온도

print(max(add_arr))