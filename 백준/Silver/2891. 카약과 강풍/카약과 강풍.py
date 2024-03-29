n, s, r = map(int, input().split())
team = list(map(int, input().split()))
boat = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    if i in team and i in boat:
        team.remove(i)
        boat.remove(i)

team.sort()
boat.sort()
for i in range(len(team)):
    if len(boat) == 0:
        break

    if abs(team[i] - boat[0]) <= 1:
        count += 1
        boat.pop(0)
    elif team[i] - boat[0] > 1:
        boat.pop(0)

print(len(team) - count)