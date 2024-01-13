n = int(input())
s = input()

sang = ["A", "B", "C"]
chang = ["B", "A", "B", "C"]
hyun = ["C", "C", "A", "A", "B", "B"]

sang_count = 0
chang_count = 0
hyun_count = 0
for i in range(n):
    if sang[i%3] == s[i]:
        sang_count += 1
    if chang[i%4] == s[i]:
        chang_count += 1
    if hyun[i%6] == s[i]:
        hyun_count += 1

result = max(max(sang_count, chang_count), hyun_count)
print(result)
if sang_count == result:
    print("Adrian")
if chang_count == result:
    print("Bruno")
if hyun_count == result:
    print("Goran")