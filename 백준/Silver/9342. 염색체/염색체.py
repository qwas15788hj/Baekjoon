t = int(input())
alpha = ["A", "B", "C", "D", "E", "F"]
for _ in range(t):
    s = input()
    arr = []

    if s[0] == "A":
        s = "B" + s
    if s[-1] == "C":
        s += "B"
    check = []
    for i in range(len(s)-1):
        check.append(s[i])
        if s[i] != s[i+1]:
            arr.append(check)
            check = []

    check.append(s[-1])
    arr.append(check)

    flag = True
    if len(arr) != 5:
        flag = False

    if len(arr[0]) != 1 or arr[0][0] != "B":
        flag = False

    for i in range(len(arr[1])):
        if arr[1][i] != "A":
            flag = False
            break

    for i in range(len(arr[2])):
        if arr[2][i] != "F":
            flag = False
            break

    for i in range(len(arr[3])):
        if arr[3][i] != "C":
            flag = False
            break

    if len(arr[-1]) != 1 or arr[-1][0] != "B":
        flag = False

    if flag:
        print("Infected!")
    else:
        print("Good")