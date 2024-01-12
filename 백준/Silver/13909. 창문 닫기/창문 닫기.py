#백준 13909번
import sys

input = sys.stdin.readline

n = int(input())
# arr = [0] * n


# 1 2 3 4 5 6 7 8 9
# o x x o x x x x o 

# 1 1 1
# 1 2 4
# 1 3 9
# 1 4 16

cnt = 0
for i in range(int(n ** (1/2))):
    cnt += 1
print(cnt)

# print((n ** (1/2)))