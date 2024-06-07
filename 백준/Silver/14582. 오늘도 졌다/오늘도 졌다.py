a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False
a_score, b_score = 0, 0
for i in range(len(a)):
    a_score += a[i]
    if a_score > b_score:
        flag = True
        break
    b_score += b[i]
    if a_score > b_score:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")