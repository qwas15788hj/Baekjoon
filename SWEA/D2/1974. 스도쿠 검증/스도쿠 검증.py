t = int(input())
for tc in range(1, t+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    x_test = [0]*10
    flag = True
    for i in range(9):
        for j in range(9):
            x_test[arr[i][j]] += 1
        for z in range(1, 10):
            if x_test[z] != i+1:
                flag = False
                break
        if flag == False:
            break

    y_test = [0]*10
    for i in range(9):
        for j in range(9):
            y_test[arr[j][i]] += 1
        for z in range(1, 10):
            if y_test[z] != i+1:
                flag = False
                break
        if flag == False:
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            test = [0]*10
            for x in range(i, i+3):
                for y in range(j, j+3):
                    test[arr[x][y]] += 1

            for s in range(1, 10):
                if test[s] != 1:
                    flag = False
                    break
            if flag == False:
                break
        if flag == False:
            break

    if flag == True:
        print("#{} {}" .format(tc, 1))
    else:
        print("#{} {}" .format(tc, 0))