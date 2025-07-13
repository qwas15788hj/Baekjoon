import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort() # 시작 위치 기준으로 정렬
answer = 0
plank = -1 # 널빤지를 마지막으로 덮은 위치
for s, e in arr:
    # 이미 널빤지로 덮인 웅덩이면 패스
    if plank >= e:
        continue
    # 아직 덮이지 않은 경우, 시작 지점 보정
    s = max(s, plank)

    # 필요한 널빤지 개수 계산
    count = (e-s)//l
    if (e-s)%l != 0:
        count += 1

    answer += count
    plank = (s + (l*count)) # 널빤지 끝 위치 갱신

print(answer)