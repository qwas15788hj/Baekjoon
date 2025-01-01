n = int(input())

arr = []
for i in range(2, 150):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        arr.append(i)

for i in range(len(arr)-1):
    if arr[i] * arr[i+1] > n:
        print(arr[i] * arr[i+1])
        break