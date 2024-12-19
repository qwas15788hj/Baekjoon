from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = input()
    arr = arr.replace("[", "")
    arr = arr.replace(",", " ")
    arr = arr.replace("]", "")
    queue = deque(list(map(int, arr.split())))

    if p.count("D") > len(queue):
        print("error")
    else:
        count = 0
        for i in p:
            if i == "R":
                count += 1
            else:
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

        if count % 2 == 0:
            print("[" + ",".join(map(str, queue)) + "]")
        else:
            a = []
            for i in queue:
                a.append(i)
            print("[" + ",".join(map(str, a[::-1])) + "]")