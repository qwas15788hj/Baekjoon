n = int(input())

def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if prime(number * 10 + i):
                dfs(number * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)