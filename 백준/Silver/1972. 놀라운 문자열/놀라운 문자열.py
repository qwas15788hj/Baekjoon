while True:
    s = input()
    if s == "*":
        break

    idx = 1
    flag = True
    for i in range(1, len(s)):
        dic = dict()
        for j in range(len(s)-i):
            if s[j] + s[j+i] in dic:
                flag = False
                break
            else:
                dic[s[j] + s[j+i]] = 1

        if flag == False:
            break

    if flag:
        print(f"{s} is surprising.")
    else:
        print(f"{s} is NOT surprising.")