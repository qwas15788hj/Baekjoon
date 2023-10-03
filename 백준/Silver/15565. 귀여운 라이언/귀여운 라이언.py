n, k = map(int, input().split()) # n, k 입력
arr = list(map(int, input().split())) # 인형 입력
answer = 1e9 # 최종 최소 길이
count = 0 # 라이언 인형 개수
left, right = 0, 0 # 왼쪽, 오른쪽 포인터

# 처음이 라이언 인형이면 count 증가
if arr[left] == 1:
    count += 1

# 둘 중 하나의 포인터가 끝까지 도달할때까지
while left < len(arr) and right < len(arr):
    if count < k: # 개수가 k 보다 적으면
        right += 1 # 오른쪽 증가
        # 증가한 오른쪽이 길이보다 작고 1이면 카운트 증가
        if right < len(arr) and arr[right] == 1:
            count += 1
    else: # 개수가 충분하다면
        if count == k: # 개수가 k개 라면
            answer = min(answer, right - left + 1) # answer 갱신
        # 왼쪽이 길이보다 작고 1이면 카운트 감소
        if left < len(arr) and arr[left] == 1:
            count -= 1
        left += 1 # left 증가

if answer == 1e9:
    print(-1)
else:
    print(answer)