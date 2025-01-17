def check(arr, eq):
    # 행 체크
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2] and arr[i][2] == eq:
            return True
    # 열 체크
    for i in range(3):
        if arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[2][i] == eq:
            return True
    # 대각선 체크
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[2][2] == eq:
        return True
    if arr[2][0] == arr[1][1] and arr[1][1] == arr[0][2] and arr[0][2] == eq:
        return True

    return False

while True:
    s = input()
    if s == "end":
        break

    arr = [["0"] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            arr[i][j] = s[i*3+j]

    x_count, o_count = 0, 0
    for i in range(3):
        x_count += arr[i].count("X")
        o_count += arr[i].count("O")

    if x_count == o_count and not check(arr, "X") and check(arr, "O"):
        print("valid")
        continue
    if x_count == o_count+1 and check(arr, "X") and not check(arr, "O"):
        print("valid")
        continue
    if x_count == 5 and o_count == 4 and not check(arr, "O"):
        print("valid")
        continue

    print("invalid")