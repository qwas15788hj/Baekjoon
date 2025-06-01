arr = ["1", "2", "3"]
def check(num):
    for i in range(-1, -len(num)//2-1, -1):
        if num[i*2:i] == num[i:]:
            return False
    return True

def func(num):
    if len(num) == n:
        print(num)
        exit()

    for i in arr:
        next_num = num + i
        if check(next_num):
            func(next_num)

n = int(input())
for i in arr:
    func(i)