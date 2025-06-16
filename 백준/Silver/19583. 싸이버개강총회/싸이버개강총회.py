import sys
input = sys.stdin.readline

s, e, q = map(str, input().split())
s = int(s[:2])*60 + int(s[3:])
e = int(e[:2])*60 + int(e[3:])
q = int(q[:2])*60 + int(q[3:])

dic = dict()
answer = 0
while True:
    try:
        t, n = map(str, input().split())
        t = int(t[:2])*60 + int(t[3:])
        if t <= s:
            dic[n] = 0
        elif e <= t <= q and n in dic:
            dic.pop(n)
            answer += 1
    except:
        break
        
print(answer)