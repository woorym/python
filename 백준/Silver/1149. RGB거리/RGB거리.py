# 백준 1149번
import sys
input = sys.stdin.readline

# 집의 수
n = int(input())
rgb = [0] * n

for i in range(n):
    rgb[i] = list(map(int, input().split()))

# print(rgb_list)
for i in range(1, n):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

# print(rgb)
num = min(rgb[n - 1][0], rgb[n - 1][1], rgb[n - 1][2])
print(num)

