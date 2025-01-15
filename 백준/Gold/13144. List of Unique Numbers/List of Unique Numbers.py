import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

num = [0] * 100001
plus = []
minus = []
left, right = 0, 0

while right != n:
    num[arr[right]] += 1 # right 값 추가
    if num[arr[right]] > 1: # 2개 이상이면
        plus.append(right - left) # 이전까지의 값 조합 개수 저장
        while num[arr[right]] > 1: # right 값 1개만 될 때까지
            num[arr[left]] -= 1 # left 값 줄이고
            left += 1 # left 증가
        minus.append(right - left) # right 값이 1개가 될 때, 겹쳐진 차이 만큼 minus에 저장

    right += 1

plus.append(right - left)

answer = 0
for p in plus:
    answer += (p * (p+1))//2
for m in minus:
    answer -= (m * (m+1))//2

print(answer)