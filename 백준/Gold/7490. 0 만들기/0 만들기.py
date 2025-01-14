import sys
input = sys.stdin.readline
from itertools import product, repeat

t = int(input())
for _ in range(t):
    n = int(input())
    arr = ["+", "-", " "]
    pro = list(product(arr, repeat=n-1))

    # "-"가 1개라도 들어간 모든 경우의 수
    check = []
    s = ""
    for i in range(len(pro)):
        if "-" in pro[i]:
            for j in range(len(pro[i])):
                s += str(j+1)
                s += pro[i][j]
            s += str(n)
            check.append(s)
        s = ""

    # 연산 결과가 0인 결과 값들
    answer = []
    for i in range(len(check)):
        num = 0
        now = check[i][0]
        op = "+"
        for j in range(1, len(check[i])):
            if check[i][j] == "+":
                if op == "+":
                    num += int(now)
                else:
                    num -= int(now)
                now = ""
                op = "+"
            elif check[i][j] == "-":
                if op == "+":
                    num += int(now)
                else:
                    num -= int(now)
                now = ""
                op = "-"
            elif check[i][j] == " ":
                pass
            else:
                now += check[i][j]

        if op == "+":
            num += int(now)
        else:
            num -= int(now)

        if num == 0:
            answer.append(check[i])

    answer.sort()
    for i in answer:
        print(i)
    print()