from collections import deque

s = input()
t = input()

queue = deque()
queue.append(t)
flag = False

while queue and not flag:
    word = queue.popleft()
    if word == s:
        flag = True
        break

    if len(word) > len(s):
        if word[-1] == "A":
            queue.append(word[:-1])
        if word[0] == "B":
            queue.append(word[1:][::-1])

if flag:
    print(1)
else:
    print(0)