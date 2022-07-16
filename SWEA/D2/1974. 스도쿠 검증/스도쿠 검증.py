t = int(input())
for tc in range(1, t+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    flag = True
    for j in range(9):
        x_test = [0]*10
        for i in range(9):
            x_test[arr[j][i]] += 1
        for z in range(1, 10):
            if x_test[z] != 1:
                flag = False
                break
        if flag == False:
            break

    for j in range(9):
        y_test = [0]*10
        for i in range(9):
            y_test[arr[i][j]] += 1
        for z in range(1, 10):
            if y_test[z] != 1:
                flag = False
                break
        if flag == False:
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s_test = [0]*10
            for z in range(i, i+3):
                for k in range(j, j+3):
                    s_test[arr[z][k]] += 1
            for m in range(1, 10):
                if s_test[m] != 1:
                    flag = False
                    break
            if flag == False:
                break
        if flag == False:
            break

    if flag == False:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")