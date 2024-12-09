import sys
input = sys.stdin.readline

month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
hour = int(time[:2])
minute = int(time[3:])

month_arr = ["January", "February", "March", "April",
             "May", "June", "July", "August", "September",
             "October", "November", "December"]
day_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    day_arr[1] += 1

total = sum(day_arr) * 24 * 60
now = (sum(day_arr[:month_arr.index(month)]) + day - 1) * 24 * 60 + hour * 60 + minute

print(now/total * 100)