t = int(input())
for _ in range(t):
    s = input()
    k = int(input())
    arr = [[] for _ in range(26)]
    for i in range(len(s)):
        arr[ord(s[i])-97].append(i)

    min_answer = 1e9
    max_answer = 0
    for a in arr:
        for i in range(len(a)-k+1):
            min_answer = min(min_answer, a[i+k-1] - a[i] + 1)
            max_answer = max(max_answer, a[i+k-1] - a[i] + 1)

    if min_answer == 1e9:
        print(-1)
    else:
        print(min_answer, max_answer)