x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
idx = 0
for i in range(x-1):
    idx += month[i]
idx += y

print(day[idx%7])