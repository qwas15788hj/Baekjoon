n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0], x[1]))
room = []
for i in range(n):
    if len(room) == 0:
        room.append(arr[i])
        continue

    if room[-1][1] > arr[i][1]:
        room.pop()
        room.append(arr[i])
    elif room[-1][1] <= arr[i][0]:
        room.append(arr[i])

print(len(room))