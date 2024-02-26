n = input()
answer = 1
idx = 0

while True:
    check = str(answer)
    for i in range(len(check)):
        if n[idx] == check[i]:
            idx += 1
        if idx == len(n):
            break

    if idx == len(n):
        break

    answer += 1

print(answer)