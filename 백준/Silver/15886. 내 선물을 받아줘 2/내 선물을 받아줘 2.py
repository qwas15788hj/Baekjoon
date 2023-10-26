n = int(input())
arr = input()
answer = 0
for i in range(len(arr) - 1):
    if arr[i:i+2] == "EW":
        answer += 1

print(answer)