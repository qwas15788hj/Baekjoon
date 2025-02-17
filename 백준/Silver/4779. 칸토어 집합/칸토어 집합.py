def cantor(x, y):
    if y == 1:
        return
    for i in range(x+y//3, x+(y//3)*2):
        answer[i] = " "
    cantor(x, y//3)
    cantor(x+(y//3)*2, y//3)

while True:
    try:
        n = int(input())
        answer = ["-"] * (3**n)
        cantor(0, 3**n)
        print("".join(answer))
    except:
        break