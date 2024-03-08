import sys
input = sys.stdin.readline

n, m = map(int, input().split())
note = set()
for _ in range(n):
    note.add(input().rstrip())

count = n
for _ in range(m):
    words = list(map(str, input().rstrip().split(",")))
    for word in words:
        if word in note:
            note.remove(word)
            count -= 1
    print(count)