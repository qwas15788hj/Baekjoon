from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tree = deque([])

    flag = True
    for i in arr:
        if flag == True:
            tree.appendleft(i)
            flag = False
        else:
            tree.append(i)
            flag = True

    answer = 0
    for i in range(len(tree)-1):
        answer = max(answer, abs(tree[i]-tree[i+1]))

    print(answer)