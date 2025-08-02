s1 = input()
s2 = input()

arr1 = [0] * 26
arr2 = [0] * 26
for i in range(len(s1)):
    arr1[ord(s1[i])-97] += 1
for i in range(len(s2)):
    arr2[ord(s2[i])-97] += 1

answer = 0
for i in range(26):
    if arr1[i] != arr2[i]:
        answer += abs(arr1[i]-arr2[i])

print(answer)