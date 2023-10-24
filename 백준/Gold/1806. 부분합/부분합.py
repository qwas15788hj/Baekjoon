n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# 누적 합 사용
for i in range(1, len(arr)):
    arr[i] += arr[i-1]

answer = 1e9
left, right = 0, 0

while left != len(arr): # 왼쪽 포인터가 끝까지 도달할 때까지
    if arr[right] - arr[left] >= s: # 오른쪽 포인터 누적합 - 왼쪽 포인터 누적합이 s보다 크거나 같으면
        answer = min(answer, right - left) # 둘 차이와 answer 중 작은 것으로 갱신
        left += 1 # 왼쪽 포인터 증가
    else: # s보다 작으면
        if right == len(arr) - 1: # 오른쪽 포인터가 끝까지 도달했다면
            left += 1 # 왼쪽 포인터 증가
        else: # 오른쪽 포인터가 끝까지 도달안했다면
            right += 1 # 오른쪽 포인터 증가

if answer == 1e9:
    print(0)
else:
    print(answer)