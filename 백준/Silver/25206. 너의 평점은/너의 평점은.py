score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
total_score = 0
total_time = 0

for _ in range(20):
    a, b, c = map(str, input().split())
    if c == "P":
        continue
    total_score += int(b[0]) * score[grade.index(c)]
    total_time += int(b[0])

print(total_score/total_time)