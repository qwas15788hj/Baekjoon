n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
answer = 0
for i in range(len(arr)):
    while stack and arr[i] >= stack[-1]: # 스택에 요소가 있고, 현재 건물이 스택의 끝 부분보다 크거나 같으면
        stack.pop() # 끝 부분 빼기
    stack.append(arr[i]) # 스택에 현재 건물 넣기

    answer += len(stack) - 1 # 남은 건물 중 맨 앞 빼고 더하기

print(answer)