import sys
input = sys.stdin.readline

def jinsu(n, p):
    num = ""
    while n > 0:
        n, mod = divmod(n, p)
        num += str(mod)
    return num[::-1]

inp = list(map(int, input().split()))
jeju = ["H", "T", "C", "K", "G"]
choco = []
for i in range(5):
    choco.append([inp[i], jeju[i]])

total = sum(inp)
m = int(input())
for _ in range(m):
    eat = list(map(int, input().split()))

    check = int(str(total)[-1])
    total -= sum(eat)
    for i in range(5):
        choco[i][0] -= eat[i]

    if (check == 0 or check == 1) or total <= 0:
        print(f'{total}7H')
    else:
        print(f'{jinsu(total, check)}7H')

    arr = sorted(choco, key=lambda x: (-x[0], x[1]))
    answer = ""
    for i in range(5):
        if arr[i][0] > 0:
            answer += arr[i][1]

    if answer == "":
        print("NULL")
    else:
        print(answer)