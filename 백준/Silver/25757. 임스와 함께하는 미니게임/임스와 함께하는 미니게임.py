n, g = map(str, input().split())
player = set()

for i in range(int(n)):
    player.add(input())

if g == "Y":
    print(len(player)//1)
elif g == "F":
    print(len(player)//2)
else:
    print(len(player)//3)