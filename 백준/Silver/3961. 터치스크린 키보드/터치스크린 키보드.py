t = int(input())
arr = [[1, 0], [2, 4], [2, 2], [1, 2], [0, 2], [1, 3], [1, 4], [1, 5], [0, 7], [1, 6],
       [1, 7], [1, 8], [2, 6], [2, 5], [0, 8], [0, 9], [0, 0], [0, 3], [1, 1], [0, 4],
       [0, 6], [2, 3], [0, 1], [2, 1], [0, 5], [2, 0]]

for _ in range(t):
    s1, l = map(str, input().split())
    answer = []
    for _ in range(int(l)):
        s2 = input()
        count = 0
        for i in range(len(s1)):
            count += abs(arr[ord(s1[i])-97][0] - arr[ord(s2[i])-97][0])
            count += abs(arr[ord(s1[i])-97][1] - arr[ord(s2[i])-97][1])

        answer.append([s2, count])

    answer.sort(key=lambda x:(x[1], x[0]))

    for a, b in answer:
        print(a, b)