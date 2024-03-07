n = int(input())
s = input()
arr = [0] * 26
answer = 0
for i in range(len(s)):
    arr[ord(s[i])-65] +=1

for _ in range(n-1):
    word = input()
    word_arr = [0] * 26
    for i in range(len(word)):
        word_arr[ord(word[i])-65] += 1

    s_count = 0
    w_count = 0
    for i in range(len(arr)):
        if arr[i] > word_arr[i]:
            s_count += arr[i] - word_arr[i]
        elif word_arr[i] > arr[i]:
            w_count += word_arr[i] - arr[i]

    if abs(s_count - w_count) <= 1 and (s_count + w_count) <= 2:
        answer += 1

print(answer)