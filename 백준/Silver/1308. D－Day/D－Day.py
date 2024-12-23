sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

flag = True
if ey > sy + 1000:
    flag = False
if ey == sy + 1000 and em > sm:
    flag = False
if ey == sy + 1000 and em == sm and ed >= sd:
    flag = False

if flag:
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    for i in range(sy+1, ey):
        answer += sum(day)
        if ((i%4 == 0 and i%100 != 0) or (i%400 == 0)):
            answer += 1
    if sy == ey:
        if sm == em:
            answer += ed - sd
        else:
            for i in range(sm-1, em-1):
                answer += day[i]
            answer -= sd
            answer += ed

            if ((sy % 4 == 0 and sy % 100 != 0) or (sy % 400 == 0)):
                if sm <= 2:
                    answer += 1
    else:
        for i in range(sm-1, 12):
            answer += day[i]
        answer -= sd

        for i in range(em-1):
            answer += day[i]
        answer += ed

        if ((sy % 4 == 0 and sy % 100 != 0) or (sy % 400 == 0)):
            if sm <= 2:
                answer += 1

        if ((ey % 4 == 0 and ey % 100 != 0) or (ey % 400 == 0)):
            if em >= 3:
                answer += 1

    print(f"D-{answer}")
else:
    print("gg")