arr = list(input())

ip = []
sub_ip = []
for i in range(len(arr)):
    if arr[i] == ":":
        if len(sub_ip):
            ip.append(sub_ip)
        sub_ip = []
    else:
        sub_ip.append(arr[i])
if len(sub_ip):
    ip.append(sub_ip)

for i in range(len(ip)):
    count = 4 - len(ip[i])
    for _ in range(count):
        ip[i].insert(0, "0")

idx = 0
check = False
for i in range(len(arr)-1):
    if arr[i] == ":":
        idx += 1
        if arr[i+1] == ":":
            check = True
            break

    if check:
        break

if check:
    if arr[0] == ":":
        idx -= 1

    count = 8 - len(ip)
    for _ in range(count):
        ip.insert(idx, ["0", "0", "0", "0"])

answer = ""
for i in range(len(ip)):
    answer += "".join(ip[i]) + ":"

print(answer[:-1])