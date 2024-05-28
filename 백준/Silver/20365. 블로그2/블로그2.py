n = int(input())
arr = list(input()) + ["X"]
red = 0
blue = 0

for i in range(n):
    if arr[i] != arr[i+1]:
        if arr[i] == "R":
            red += 1
        else:
            blue += 1

print(min(red, blue) + 1)