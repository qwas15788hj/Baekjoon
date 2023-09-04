import sys
input = sys.stdin.readline

n = int(input()) # n 입력
arr = [0] + list(map(int, input().split())) # 누적합을 위해 입력 리스트에 0을 맨앞에 추가
m = int(input()) # m 입력
# 배열 누적합으로 변환
for i in range(1, len(arr)):
    arr[i] += arr[i-1]

# 누적합 배열을 통해 값 출력
for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])