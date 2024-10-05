answer = []
while True:
    s = input()
    if s[0] == "-":
        break

    arr = []
    for i in range(len(s)):
        if s[i] == "{":
            arr.append(s[i])
        else:
            if len(arr) and arr[-1] == "{":
                arr.pop()
            else:
                arr.append(s[i])

    count = 0
    for i in range(0, len(arr), 2):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            count += 2

    answer.append(count)

for i in range(len(answer)):
    print(f'{i+1}. {answer[i]}')