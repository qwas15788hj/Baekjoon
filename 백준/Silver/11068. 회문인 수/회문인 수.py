t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(2, 65):
        check = []
        temp = n
        while temp != 0:
            check.append(temp % i)
            temp //= i

        for j in range(len(check)//2):
            if check[j] != check[-1-j]:
                arr.append(0)
                break

    if len(arr) == 63:
        print(0)
    else:
        print(1)