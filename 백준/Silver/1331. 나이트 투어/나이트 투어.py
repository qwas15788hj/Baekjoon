arr = [input() for _ in range(36)]
s = set()
s.add(arr[0])
flag = True
for i in range(1, 36):
    a1, a2 = ord(arr[i-1][0]), int(arr[i-1][1])
    n1, n2 = ord(arr[i][0]), int(arr[i][1])
    if not ((abs(a1-n1) == 1 and abs(a2-n2) == 2) or (abs(a1-n1) == 2 and abs(a2-n2) == 1)):
        flag = False
    s.add(arr[i])

if len(s) != 36:
    flag = False


a1, a2 = ord(arr[0][0]), int(arr[0][1])
n1, n2 = ord(arr[-1][0]), int(arr[-1][1])
if (abs(a1 - n1) + abs(a2 - n2)) != 3:
    flag = False

if flag:
    print("Valid")
else:
    print("Invalid")