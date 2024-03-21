n = int(input())
arr = list(input())
red = arr.count("R")
blue = arr.count("B")

answer = []
for i in range(red):
    if arr[i] == "B":
        answer.append(red-i)
        break
else:
    answer.append(0)

for i in range(-1, -(red+1), -1):
    if arr[i] == "B":
        answer.append(red+1+i)
        break
else:
    answer.append(0)

for i in range(blue):
    if arr[i] == "R":
        answer.append(blue-i)
        break
else:
    answer.append(0)

for i in range(-1, -(blue+1), -1):
    if arr[i] == "R":
        answer.append(blue+1+i)
        break
else:
    answer.append(0)

print(min(answer))