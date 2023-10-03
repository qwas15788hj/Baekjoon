n = int(input()) # n 입력
t = [] # 상담 별 걸리는 요일 저장 배열
p = [] # 상담 별 이익 저장 배열
# 상담 별 요일과 이익 입력 후 저장
for _ in range(n):
    t1, p1 = map(int, input().split())
    t.append(t1)
    p.append(p1)

arr = [0] * (n+1) # dp 사용할 배열 n+1만큼 생성
for i in range(n-1, -1, -1): # 끝 부분부터 처음까지
    if t[i] + i > n: # 오늘 상담 걸리는 요일 + 오늘 요일이 n보다 크면
        arr[i] = arr[i+1] # 상담 못함으로 이전 이익 저장
    else: # 오늘 상담이 가능하다면
        # 이전 상담, 오늘 상담함으로써 이익 + 오늘 상담함으로써 이전까지 요일 중 큰 값으로 저장
        arr[i] = max(arr[i+1], arr[t[i] + i] + p[i])

print(arr[0])