n = int(input())
arr = []
for _ in range(n):
    s = input()
    sub = []
    for i in s:
        sub.append(i)
    arr.append(sub)

head_x, head_y = 0, 0
flag = False
for i in range(n):
    for j in range(len(arr)):
        if arr[i][j] == "*":
            head_x, head_y = i, j
            flag = True
            break
    if flag:
        break

heart_x, heart_y = head_x+1, head_y
left_hand, right_hand, waist, left_leg, right_leg = 0, 0, 0, 0, 0

for i in range(heart_y):
    if arr[heart_x][i] == "*":
        left_hand += 1

for i in range(heart_y+1, len(arr)):
    if arr[heart_x][i] == "*":
        right_hand += 1

for i in range(heart_x+1, len(arr)):
    if arr[i][heart_y] == "*":
        waist += 1

for i in range(heart_x + waist + 1, len(arr)):
    if arr[i][heart_y-1] == "*":
        left_leg += 1
    if arr[i][heart_y+1] == "*":
        right_leg += 1

print(heart_x+1, heart_y+1)
print(left_hand, right_hand, waist, left_leg, right_leg)