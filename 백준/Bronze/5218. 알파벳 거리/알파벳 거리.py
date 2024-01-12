n = int(input())
for _ in range(n):
    s1, s2 = map(str, input().split())
    answer = []
    for i in range(len(s1)):
        num = ord(s2[i]) - ord(s1[i])
        if num < 0:
            num += 26
        answer.append(num)

    print("Distances: ", end="")
    for a in answer:
        print(a, end=" ")
    print()