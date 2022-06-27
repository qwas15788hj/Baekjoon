from collections import Counter

arr = list(map(int, input().split()))
val = Counter(arr).most_common()

if val[0][1] == 3:
    money = 10000 + val[0][0]*1000
elif val[0][1] == 2:
    money = 1000 + val[0][0]*100
else:
    val.sort(key=lambda x:-x[0])
    money = val[0][0]*100

print(money)