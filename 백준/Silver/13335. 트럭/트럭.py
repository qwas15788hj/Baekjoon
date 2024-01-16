n, w, l = map(int, input().split())
arr = list(map(int, input().split()))
time, count = 0, 0

bridge = [0] * w

while count != n:
    out = bridge.pop(0)
    if out != 0:
        count += 1

    if len(arr):
        if sum(bridge) + arr[0] <= l:
            bridge.append(arr.pop(0))
        else:
            bridge.append(0)

    time += 1

print(time)