n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

answer = 0
stack = []
for i in range(n):
    # 스택에 비었다면 넣기
    if not stack:
        stack.append(arr[i][1])
        continue

    # 0이면 이전까지의 건물 개수 체크, stack 초기화
    if arr[i][1] == 0:
        answer += len(stack)
        stack = []
        continue

    # stack의 마지막 건물이 이제 들어올 건물보다 크다면
    if stack[-1] > arr[i][1]:
        # 해당 건물보다 큰 것들 빼기
        while stack:
            if stack[-1] > arr[i][1]:
                stack.pop()
                answer += 1
            else:
                break
        # stack이 비었거나, 마지막 건물과 길이가 같지 않다면 추가
        if not stack:
            stack.append(arr[i][1])
        else:
            if stack[-1] != arr[i][1]:
                stack.append(arr[i][1])

    # stack의 마지막 건물과 길이가 같다면 pass
    elif stack[-1] == arr[i][1]:
        pass
    # stack의 마지막 건물보다 크면 stack에 추가
    else:
        stack.append(arr[i][1])

for s in stack:
    if s > 0:
        answer += 1

print(answer)