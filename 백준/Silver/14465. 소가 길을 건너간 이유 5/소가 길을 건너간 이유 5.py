n, k, b = map(int, input().split())
arr = [1] * (n+1) # 총 n+1개의 신호등이 켜진 상태로 배열 생성
for _ in range(b):
    arr[int(input())] = 0 # 꺼진 신호등 끄기

start = 1 # 시작점
end = k # 끝점
count = arr[start : end+1].count(0) # 현재 체크할 처음 ~ 끝지점까지 꺼진 신호등 수
answer = count # 최종 필요한 신호등 수, 최초 처음 지점

for i in range(n - k):
    start += 1 # 시작점 오른쪽으로 한칸 이동
    # 이동 전 신호등이 꺼져있다면 하나 줄이기
    if arr[start - 1] == 0:
        count -= 1

    end += 1 # 끝 지점 오른쪽으로 한칸 이동
    # 이동 후 신호등이 꺼져있다면 하나 늘리기
    if arr[end] == 0:
        count += 1

    answer = min(answer, count)

print(answer)