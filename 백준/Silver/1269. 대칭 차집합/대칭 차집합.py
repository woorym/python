import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))

total = len(set1 - set2) + len(set2 - set1)

print(total)