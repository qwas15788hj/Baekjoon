import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
else:
    time = 0
    while True:
        for i in range(n):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    box.pop(j)
                    break

        time += 1
        if len(box) == 0:
            break

    print(time)