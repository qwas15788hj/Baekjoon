n, m = map(int, input().split()) # 과목 수 n, 주어진 마일리지 m 입력
arr = [] # 과목별 필요한 최소 마일리지 저장할 배열
for _ in range(n):
    p, l = map(int, input().split()) # 신청한 사람 p, 과목의 수강인원 l 입력
    mile = list(map(int, input().split())) # 신청한 사람들의 마일리지 입력

    if p >= l: # 신청한 사람이 수강인원보다 크거나 같으면
        mile.sort(reverse=True) # 마일리지 내림차순
        arr.append(mile[l-1]) # 신청한 사람들 중 수강인원 수와 맞는 마일리지 사용
    else: # 수강인원이 크면
        arr.append(1) # 1 마일리지만 사용

arr.sort() # 과목별로 필요한 최소 마일리지 정렬
idx = 0 # 현재 과목
answer = 0 # 과목 수
while idx < len(arr):
    if arr[idx] > m: # 현재 과목이 가지고 있는 마일리지보다 크면 수강 실패, 종료
        break
    else: # 가지고 있는 마일리지가 더 많다면
        m -= arr[idx] # 해당 과목 마일리지 빼고
        idx += 1 # 다음 과목으로
        answer += 1 # 과목 수강 신청 성공

print(answer)