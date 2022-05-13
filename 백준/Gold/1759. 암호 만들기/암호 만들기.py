import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

answer = []
words = list(combinations(arr, n))
for word in words:
    count = 0
    for w in word:
        if w in vowels:
            count += 1
  
    if count >= 1 and n-count >= 2:
        answer.append("".join(sorted(word)))

for i in sorted(answer):
    print(i)