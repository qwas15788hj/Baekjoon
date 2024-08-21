n = int(input())
arr = set()
arr.add("ChongChong")
for _ in range(n):
    a, b = map(str, input().split())
    if a in arr and b not in arr:
        arr.add(b)
    if a not in arr and b in arr:
        arr.add(a)

print(len(arr))