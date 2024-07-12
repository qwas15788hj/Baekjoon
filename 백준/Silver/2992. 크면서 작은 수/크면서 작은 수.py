x = int(input())
answer = 0
arr = [0] * 10
for i in range(len(str(x))):
    arr[int(str(x)[i])] += 1

for i in range(10**(len(str(x))-1), 10**len(str(x))):
    check = [0] * 10
    for j in range(len(str(i))):
        check[int(str(i)[j])] += 1

    if arr == check and i > x:
        answer = i
        break

print(answer)