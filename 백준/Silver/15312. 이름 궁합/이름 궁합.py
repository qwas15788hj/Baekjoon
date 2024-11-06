a = input()
b = input()
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

arr = []
for i in range(len(a)):
    arr.append(alpha[ord(a[i])-65])
    arr.append(alpha[ord(b[i])-65])

for i in range(len(arr)-2):
    for j in range(len(arr)-1):
        arr[j] = (arr[j]+arr[j+1])%10
    arr.pop()

answer = str(arr[0]*10+arr[1])
if len(answer) == 2:
    print(answer)
else:
    print("0"+answer)