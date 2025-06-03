import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

count = [0] * n # 보이는 갯수
near = [1e9] * n # 가장 가까운 건물

# 오른쪽 건물 체크
stack = []
for i in range(n):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    count[i] += len(stack)

    if stack:
        near[i] = stack[-1]
    stack.append(i)

# 왼쪽 건물 체크
stack = []
for i in range(n-1, -1, -1):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    count[i] += len(stack)

    if stack:
        if abs(i-stack[-1]) < abs(i-near[i]):
            near[i] = stack[-1]
    stack.append(i)

# 출력
for i in range(n):
    if count[i] > 0:
        print(count[i], near[i]+1)
    else:
        print(count[i])