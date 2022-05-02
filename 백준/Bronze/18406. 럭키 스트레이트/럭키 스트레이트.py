n = list(map(int, input()))
if sum(n[:int(len(n)/2)]) == sum(n[int(len(n)/2):]):
    print("LUCKY")
else:
    print("READY")