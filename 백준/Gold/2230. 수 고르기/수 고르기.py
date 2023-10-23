import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort() # 입력 배열 정렬

answer = arr[-1] - arr[0] # 초기 값이 1e9 보다 클 수 있으므로 가장 큰 값 - 가장 작은 값으로
start, end = 0, 0 # 시작, 끝 지점 / 투포인터 사용

# start가 끝까지 도달할때 까지 반복
while start != len(arr):
    if arr[end] - arr[start] >= m: # end 와 start 차이가 m 이상이면
        answer = min(answer, arr[end] - arr[start]) # answer 갱신
        start += 1 # start 오른쪽으로 이동
    else: # end, start 차이가 m 미만이면
        if end == len(arr) - 1: # end가 이미 끝 지점에 도달했으면
            start += 1 # start 이동
        else: # end가 끝 지점에 도달하지 않았다면
            end += 1 # end 이동

print(answer)