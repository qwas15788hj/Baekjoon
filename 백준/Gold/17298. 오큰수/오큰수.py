n = int(input())
arr = list(map(int, input().split()))

stack = []
answer = []
for i in range(n-1, -1, -1):
    while True:
        if stack:
            if stack[-1] > arr[i]:
                answer.append(stack[-1])
                stack.append(arr[i])
                break
            else:
                stack.pop()
        else:
            answer.append(-1)
            stack.append(arr[i])
            break

print(*answer[::-1])