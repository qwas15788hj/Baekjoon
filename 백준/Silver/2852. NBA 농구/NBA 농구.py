n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

arr.append(['3', '48:00'])
team1, team2 = 0, 0
win1, win2 = 0, 0
time = 0
for i in range(n+1):
    t = int(arr[i][1][:2])*60 + int(arr[i][1][3:])
    if team1 > team2:
        win1 += (t-time)
    elif team1 < team2:
        win2 += (t-time)
    time = t

    if arr[i][0] == "1":
        team1 += 1
    elif arr[i][0] == "2":
        team2 += 1

h1, m1 = str(win1//60), str(win1%60)
h2, m2 = str(win2//60), str(win2%60)
if len(h1) == 1:
    h1 = "0" + h1
if len(m1) == 1:
    m1 = "0" + m1
if len(h2) == 1:
    h2 = "0" + h2
if len(m2) == 1:
    m2 = "0" + m2

print(f"{h1}:{m1}")
print(f"{h2}:{m2}")