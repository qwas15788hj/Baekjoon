import sys
input = sys.stdin.readline

arr = []
for i in range(1, 9):
    arr.append([int(input()), i])
arr.sort(key=lambda x:-x[0])

answer = 0
li = []
for i in range(5):
    answer += arr[i][0]
    li.append(arr[i][1])
li.sort()

print(answer)
print(*li)