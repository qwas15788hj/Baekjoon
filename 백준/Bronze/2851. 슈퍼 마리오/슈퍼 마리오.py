arr = [int(input()) for _ in range(10)]

num = 0
answer = 0
for i in range(10):
    if abs(100-num) >= abs(100-(num+arr[i])):
        answer = num + arr[i]
    num += arr[i]

print(answer)