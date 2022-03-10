import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
answer = list(sorted(set(array)))

print(*answer)