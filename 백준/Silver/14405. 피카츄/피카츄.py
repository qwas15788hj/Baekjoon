s = input()
arr = ["pi", "ka", "chu"]
word = ""
for i in range(len(s)):
    word += s[i]
    if word in arr:
        word = ""

if word == "":
    print("YES")
else:
    print("NO")