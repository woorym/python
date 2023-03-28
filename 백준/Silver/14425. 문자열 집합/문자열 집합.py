import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

set_dict = {}

for i in range(n):
    set_str = input()

    set_dict[set_str] = 0

check_list = []
for i in range(m):
    check_str = input()

    if check_str in set_dict.keys():
        set_dict[check_str] += 1

total = 0
for k in set_dict.values():
    total += k

print(total)