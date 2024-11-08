n = int(input())
arr = input().split()

dic = dict()
for i in range(n):
    if len(arr[i]) >= 6 and arr[i][-6:] == "Cheese":
        dic[arr[i]] = 1

if len(dic) >= 4:
    print("yummy")
else:
    print("sad")