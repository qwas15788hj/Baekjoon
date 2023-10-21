a, b, c = map(int, input().split())
answer = max(int(a * b / c), int(a / b * c))
print(answer)