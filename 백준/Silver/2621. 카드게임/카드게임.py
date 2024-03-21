color, num = [], []
for _ in range(5):
    c, n = map(str, input().split())
    color.append(c)
    num.append(int(n))

num.sort()
answer = []
flag = True
for i in range(len(num) - 1):
    if num[i + 1] - num[i] != 1:
        flag = False
        break

# 1.
if len(set(color)) == 1 and flag:
    answer.append(max(num)+900)

# 2.
for i in range(1, 10):
    if num.count(i) == 4:
        answer.append(i+800)
        break

# 3.
check = []
for i in range(1, 10):
    if num.count(i) != 0:
        check.append([num.count(i), i])
check.sort(key=lambda x:(x[0], x[1]))
if len(check) == 2 and check[0][0] == 2:
    answer.append(check[1][1]*10 + check[0][1]+700)

# 4.
if len(set(color)) == 1:
    answer.append(max(num)+600)

# 5.
if flag:
    answer.append(max(num)+500)

# 6.
if len(check) == 3 and check[-1][0] == 3:
    answer.append(check[-1][1]+400)

# 7.
if len(check) == 3 and check[-1][0] == 2 and check[-2][0] == 2:
    answer.append(check[-1][1]*10 + check[-2][1]+300)

# 8.
if len(check) == 4:
    answer.append(check[-1][1]+200)

# 9.
if len(answer) == 0:
    answer.append(max(num)+100)

print(max(answer))