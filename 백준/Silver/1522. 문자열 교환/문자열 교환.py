s = input()
count = s.count("a")
answer = 1e9
left = 0

while left < len(s):
    right = left + count
    if right > len(s):
        temp = s[left:len(s)] + s[:right-len(s)]
    else:
        temp = s[left:right]

    answer = min(answer, temp.count("b"))
    left += 1

print(answer)