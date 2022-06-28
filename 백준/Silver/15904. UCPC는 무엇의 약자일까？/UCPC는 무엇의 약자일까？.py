s = input()
alpha = ["U", "C", "P", "C"]

i = 0
for alp in alpha:
    if alp in s:
        i += 1
        s = s[s.index(alp)+1:]
    else:
        print("I hate UCPC")
        break

if i == 4:
    print("I love UCPC")