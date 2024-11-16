b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

n = min(min(b, c), d)
cost = 0
for i in range(n):
    cost += burger[i] + side[i] + drink[i]
cost *= 0.9
for i in range(n, b):
    cost += burger[i]
for i in range(n, c):
    cost += side[i]
for i in range(n, d):
    cost += drink[i]

print(sum(burger) + sum(side) + sum(drink))
print(int(cost))