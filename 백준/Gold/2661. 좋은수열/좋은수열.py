arr = ["1", "2", "3"]

# 좋은 수열인지 확인
def check(num):
    for i in range(-1, -len(num)//2-1, -1):
        # 뒤쪽 i길이 부분과 바로 앞쪽 i길이 부분이 같으면 안 됨
        if num[i*2:i] == num[i:]:
            return False
    return True

# 백트래킹을 통해 수열 구성
def func(num):
    if len(num) == n:
        print(num)
        exit() # 사전순 가장 앞선 수열 출력 후 종료

    for i in arr:
        next_num = num + i
        if check(next_num):
            func(next_num)

# 입력 및 초기 시작
n = int(input())
for i in arr:
    func(i)