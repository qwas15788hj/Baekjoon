while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n%i == 0:
            arr.append(i)

    answer = str(n) + " = 1"
    if sum(arr) == n:
        for i in range(1, len(arr)):
            answer += " + " + str(arr[i])
        print(answer)
    else:
        print(str(n) + " is NOT perfect.")