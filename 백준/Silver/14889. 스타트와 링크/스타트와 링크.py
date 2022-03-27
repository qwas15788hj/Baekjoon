from itertools import combinations
n = int(input())
member = [i for i in range(n)]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = list(combinations(member, int(n/2)))

answer = int(1e9)
for r1 in result:
    start_team, link_team = 0, 0
    r2 = list(set(member)-set(r1))
    start = list(combinations(r1, 2))
    link = list(combinations(r2, 2))
    for s in start:
        start_team += arr[s[0]][s[1]]
        start_team += arr[s[1]][s[0]]
    for l in link:
        link_team += arr[l[0]][l[1]]
        link_team += arr[l[1]][l[0]]
    answer = min(answer, abs(start_team-link_team))
print(answer)