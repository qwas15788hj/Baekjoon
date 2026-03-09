n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(road):
    i, count = 0, 1 # 현재 위치, 경사로 놓을 수 있는 길 수
    while i < n-1:
        diff = road[i] - road[i+1] # 다음 길과 높이 차이

        # 평지
        if diff == 0:
            i += 1
            count += 1
        # 내리막
        elif diff == 1:
            # 내리막 경사로 놓을 수 있는지 체크
            for j in range(1, l+1):
                if i+j >= n or road[i+1] != road[i+j]:
                    return False
            i += l
            count = 0
        # 오르막
        elif diff == -1:
            if count >= l:
                i += 1
                count = 1
            else:
                return False
        # 높이 2차이 이상
        else:
            return False

    return True

answer = 0
for i in range(n):
    if check(arr[i]):
        answer += 1
for i in range(n):
    a = []
    for j in range(n):
        a.append(arr[j][i])
    if check(a):
        answer += 1

print(answer)