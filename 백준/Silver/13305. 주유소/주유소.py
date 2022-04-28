n = int(input())
dis = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_gas = gas[0]
answer = 0

for i in range(len(dis)):
    if gas[i] < min_gas:
        min_gas = gas[i]
    answer += min_gas*dis[i]
print(answer)