n = int(input())
arr = [input() for _ in range(n)]

dic = dict()
for i in range(n):
    word = arr[i]
    flag = False
    for j in range(len(word)):
        s = word[j:] + word[:j]
        if s in dic:
            flag = True
            break

    if not flag:
        dic[word] = 1

print(len(dic))