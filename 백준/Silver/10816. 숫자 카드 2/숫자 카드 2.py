import sys, math
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def count_by_range(n_list, left_value, right_value):
    right_index = bisect_right(n_list, right_value)
    left_index = bisect_left(n_list, left_value)
    return right_index - left_index

for i in range(m):
    print(count_by_range(n_list, m_list[i], m_list[i]), end=" ")