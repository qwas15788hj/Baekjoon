import sys
input = sys.stdin.readline

while True:
    try:
        s, t = map(str, input().split())

        idx = 0
        for i in range(len(t)):
            if idx == len(s):
                break
            if s[idx] == t[i]:
                idx += 1

        if idx == len(s):
            print("Yes")
        else:
            print("No")

    except:
        break