s = input()

answer = 0
arr = ["q", "u", "a", "c", "k"]
sound = [0] * 5
flag = True

count = 0
for i in range(len(s)):
    idx = arr.index(s[i])
    sound[idx] += 1
    if s[i] == "q":
        count += 1
        answer = max(answer, count)
    else:
        if sound[idx-1] == 0:
            flag = False
            break
        sound[idx-1] -= 1

        if s[i] == "k":
            count -= 1

if flag and sum(sound[:4]) == 0:
    print(answer)
else:
    print(-1)