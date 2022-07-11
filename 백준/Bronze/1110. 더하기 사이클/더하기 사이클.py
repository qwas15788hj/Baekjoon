n = input()

if int(n) < 10:
    n = "0"+n

result = n[1] + str(int(n[0]) + int(n[1]))[-1]
count = 1

while result != n:
    result = result[1] + str(int(result[0]) + int(result[1]))[-1]
    count += 1
    
print(count)