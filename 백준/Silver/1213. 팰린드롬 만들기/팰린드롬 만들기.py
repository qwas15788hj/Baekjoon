s = input()
arr = [0]*26
for i in s:
    arr[ord(i)-65] += 1

answer = ""
center = ""
odd = 0
for i in range(len(arr)):
    if arr[i]%2 != 0:
        odd += 1
        center += chr(i+65)
    answer += chr(i+65)*(arr[i]//2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer+center+answer[::-1])