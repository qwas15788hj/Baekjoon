n = int(input())
answer = 0
num = 0
left, right = 0, 0

while right < n+1:
    if num > n:
        num -= left
        left += 1
    elif num < n:
        right += 1
        num += right
    else:
        answer += 1
        right += 1
        num += right

print(answer)