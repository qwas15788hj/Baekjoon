n = int(input())
m = int(input())
arr = list(map(int, input().split()))
num = [0] * m # 0 ~ m-1 까지 재료가 있는지 체크할 배열 생성
answer = 0

# arr 원소가 m보다 작으면 해당 번호에 맞게 재료 체크
for i in range(n):
    if arr[i] < m:
        num[arr[i]] = 1

# 1 ~ m-1 까지 돌면서
for i in range(1, m):
    # m 이 되기 위해 현재 재료인 i 와 m-i 재료가 둘 다 있다면 성공
    if num[i] == 1 and num[m-i] == 1:
        answer += 1

print(answer//2) # 같은 조합이 2번 나옴으로 2로 나눈 후 출력