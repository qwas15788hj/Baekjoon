arr = ["a", "e", "i", "o", "u"]
while True:
    s = input()
    if s == "end":
        break

    # 1. 모음이 하나는 포함되어야한다
    flag1 = False
    for i in s:
        if i in arr:
            flag1 = True
            break

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
    flag2 = True
    count = 1
    check = True
    if s[0] in arr:
        check = True
    else:
        check = False

    for i in range(1, len(s)):
        if check:
            if s[i] in arr:
                count += 1
            else:
                count = 1
                check = False
        else:
            if s[i] in arr:
                count = 1
                check = True
            else:
                count += 1

        if count == 3:
            flag2 = False
            break

    # 3. 같은 글자가 연속적으로 두번 오면 안된다. (ee, oo는 허용)
    flag3 = True
    for i in range(1, len(s)):
        if s[i-1] == s[i] and (s[i] != "e" and s[i] != "o"):
            flag3 = False
            break

    if flag1 and flag2 and flag3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')