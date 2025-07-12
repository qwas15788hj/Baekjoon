s = input().rstrip()

java = False
c = False
count = 0
for i in range(len(s)):
    if s[i] == "_":
        c = True
    if "A" <= s[i] <= "Z":
        java = True
        count += 1

flag = True
for i in range(len(s)-1):
    if s[i] == "_" and s[i+1] == "_":
        flag = False
if s[0] == "_":
    flag = False
if s[-1] =="_":
    flag = False
if "A" <= s[0] <= "Z":
    flag = False

arr = []
if (java and c) or not flag:
    s = "Error!"
elif java and not c:
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            arr.append(i)
    arr = arr[::-1]
    for idx in arr:
        s = s[:idx] + "_" + chr(ord(s[idx])+32) + s[idx+1:]
elif c and not java:
    for i in range(len(s)):
        if s[i] == "_":
            arr.append(i)
    arr = arr[::-1]
    for idx in arr:
        s = s[:idx] + chr(ord(s[idx+1])-32) + s[idx+2:]

print(s)