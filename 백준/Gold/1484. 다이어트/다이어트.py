n = int(input())

finish = (n//2)+1
left, right = 1, 1
answer = []
while right <= finish:
    target = (right**2) - (left**2)
    if target == n:
        answer.append(right)

    if target > n:
        left += 1
    else:
        right += 1

if len(answer):
    for a in answer:
        print(a)
else:
    print(-1)