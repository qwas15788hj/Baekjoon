t = int(input())
for _ in range(t):
    m = input()
    dic = dict()
    flag = True

    for i in range(len(m)):
        if m[i] not in dic:
            dic[m[i]] = 1
        else:
            dic[m[i]] += 1
            if dic[m[i]] == 3:
                if i+1 >= len(m):
                    flag = False
                    break
                elif m[i+1] != m[i]:
                    flag = False
                    break
                else:
                    dic[m[i]] = -1

        if not flag:
            break

    if flag:
        print("OK")
    else:
        print("FAKE")